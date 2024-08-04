from flask import Flask, request, jsonify
from flask_cors import CORS

import hubspot
from hubspot.crm.tickets import ApiException

import pinecone
from pinecone import Pinecone, ServerlessSpec

import openai
from openai import OpenAI

import os


app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
CORS(app, resources={r"/*": {"origins": "*"}})

client = OpenAI(api_key="sk-t9kHlq70OHZB_6pCu5zGaT0MhO8kCqWoBWNrojMJ_GT3BlbkFJXTX71ff5CE_kTtKBl3XHWTFc5hSG1yQ4ea6Vj5OIwA")

def create_pinecone_index():
    data = request.json
    pineconeKey = data.get('pineconeKey')
    if not pineconeKey:
        return jsonify({"error": "API key is required"}), 400
        
    try:
        pc = Pinecone(api_key=pineconeKey)
    
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


@app.route('/', methods=['POST'])
def get_tickets():

    data = request.json
    hubspotKey = data.get('hubspotKey')
    if not hubspotKey:
        return jsonify({"error": "API key is required"}), 400
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

        create_index_response, status_code = create_pinecone_index()
        if status_code != 200:
            return jsonify(create_index_response), 500
            
        faqs = format_tickets_to_faqs(formatted_tickets)
        myFAQs = group_faqs(faqs)

        faq_folder_path = os.path.join(os.getcwd(), 'src', 'routes', 'faqDocs')
        os.makedirs(faq_folder_path, exist_ok=True)
        faq_file_path = os.path.join(faq_folder_path, 'myFAQs.txt')

        with open(faq_file_path, "w") as file:
            file.write(myFAQs)

        return jsonify({"myFAQs": myFAQs})

    except ApiException as e:
        # Handle exceptions and return an error message
        error_message = f"Exception when calling TicketsApi->get_page: {e}\n"
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)






