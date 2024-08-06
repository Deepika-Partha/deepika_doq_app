from flask import Flask, request, jsonify  # type: ignore
from flask_cors import CORS # type: ignore

import hubspot # type: ignore
from hubspot.crm.tickets import ApiException   # type: ignore 

import pinecone # type: ignore
from pinecone import Pinecone, ServerlessSpec   # type: ignore

import openai  # type: ignore
from openai import OpenAI # type: ignore

import os


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

client = OpenAI(api_key="sk-t9kHlq70OHZB_6pCu5zGaT0MhO8kCqWoBWNrojMJ_GT3BlbkFJXTX71ff5CE_kTtKBl3XHWTFc5hSG1yQ4ea6Vj5OIwA")

@app.route('/', methods=['POST'])
def main():
    data = request.json
    hubspotKey = data.get('hubspotKey')
    if not hubspotKey:
        return jsonify({"error": "API key is required"}), 400
    
    data = request.json
    pineconeKey = data.get('pineconeKey')
    if not pineconeKey:
        return jsonify({"error": "API key is required"}), 400
    
    formatted_tickets = get_tickets(hubspotKey)
    faqs = format_tickets_to_faqs(formatted_tickets)
    myFAQs = group_faqs(faqs)

    create_index_response, status_code = create_pinecone_index(pineconeKey)
    if status_code != 200:
        return jsonify(create_index_response), 500
    
    upsert_tickets(pineconeKey, formatted_tickets)

    return jsonify({"myFAQs": myFAQs})

def upsert_tickets(pineconeKey, formatted_tickets):

    try:
        pc = Pinecone(api_key=pineconeKey, environment="us-east-1")
        index = pc.Index('doq-query')

        for ticket in formatted_tickets:
            content_to_embed = ticket.get('content', '')

            if content_to_embed:
                response = client.embeddings.create(input=content_to_embed, model="text-embedding-3-small")
                embedding = response.data[0].embedding

                metadata = {
                    "subject": ticket.get('subject', ''),
                    "content": ticket.get('content', '')
                }
                
                unique_id = f"{ticket.get('subject', '')}_{ticket.get('content', '')}"
                index.upsert([{"id": unique_id, "values": embedding, "metadata": metadata}])

        vectors = []

        for ticket in formatted_tickets:
            vector_item = {}
            vector_item["id"] = ticket.id
            vector_item["metadata"] = metadata = {"subject": ticket.properties.get('subject', ''),"content": ticket.properties.get('content', '')}
            vector_item["values"] = embedding
            vectors.append(vector_item)

            upsert_response = index.upsert(
                vectors = vectors,
                namespace="example-namespace"
            )
    except Exception as e:
        print(f"Error during upsert_tickets: {e}")
    

def create_pinecone_index(pineconeKey):
    api_key = pineconeKey
    try:
        pc = Pinecone(api_key=api_key)
        pc.create_index(
            name="doq-query",
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
        return {"message": "Index created successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 500

def format_tickets_to_faqs(tickets):
    faqs = []
    for ticket in tickets:
        subject = ticket.get('subject', 'No Subject')
        content = ticket.get('content', 'No Content')
        faq = f"**Q: {subject}**\nA: {content}\n\n"
        faqs.append(faq)
    return faqs


def group_faqs(faqs):
    myFAQs = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Group the following FAQs based on their topics:"},
            {"role": "user", "content": "\n".join(faqs)}
        ]
    )
    return myFAQs.choices[0].message.content


def get_tickets(hubspotKey):

    client = hubspot.Client.create(access_token=hubspotKey)
    try:
        limit = 10
        after = None
        properties = ["subject", "content"]

        api_response = client.crm.tickets.basic_api.get_page(
            limit=limit,
            after=after,
            properties=properties
        )

        tickets = api_response.results
        formatted_tickets = [
            {
                'subject': ticket.properties.get('subject', 'N/A'),
                'content': ticket.properties.get('content', 'N/A')
            }
            
            for ticket in tickets
        ]
        return formatted_tickets
    
    except ApiException as e:
        error_message = f"Exception when calling TicketsApi->get_page: {e}\n"
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)






