from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore

import hubspot # type: ignore
from hubspot.crm.tickets import ApiException # type: ignore

import openai   # type: ignore
from openai import OpenAI   # type: ignore

import os


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

client = OpenAI(api_key="API_KEY")

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
    api_key = data.get('api_key')
    if not api_key:
        return jsonify({"error": "API key is required"}), 400
    client = hubspot.Client.create(access_token=api_key)
   
    
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

        faqs = format_tickets_to_faqs(formatted_tickets)
        myFAQs = group_faqs(faqs)

        faq_folder_path = os.path.join(os.getcwd(), 'src', 'routes', 'faqDocs')
        os.makedirs(faq_folder_path, exist_ok=True)
        faq_file_path = os.path.join(faq_folder_path, 'myFAQs.txt')

        with open(faq_file_path, "w") as file:
            file.write(myFAQs)

        return jsonify({"myFAQs": myFAQs})

    except ApiException as e:
        error_message = f"Exception when calling TicketsApi->get_page: {e}\n"
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)






