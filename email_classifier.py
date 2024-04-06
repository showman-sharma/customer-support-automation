import requests
from cohere.client import Client
import subprocess
import time
import json

# Initialize Cohere client with your API key
cohere_client = Client('u49Hv2HjZCt17mNRirq6lC20BlOEXdkb6Rebri23')  # Replace <<apiKey>> with your actual API key

# Fetch emails using the fetch_emails API from gmail_api.py
def fetch_emails():
    response = requests.get('http://127.0.0.1:5000/fetch_emails')  # Update the URL as per your API
    if response.status_code == 200:  
        emails = response.json()
        return emails
    else: 
        print("Failed to fetch emails. Status code:", response.status_code)
        return []  

# Classify emails using Cohere client
def classify_emails(emails):
    classified_emails = []
    examples = [
        {"input": "How do I find my insurance policy?", "label": "Policy Inquiry"},
        {"input": "How do I download a copy of my insurance policy?", "label": "Policy Download"}
    ]
    for email in emails:
        input_text = email['body'].strip()  # Strip any leading/trailing whitespace
        if input_text:  # Check if input text is not empty
            try:
                # Pass examples with at least two classes
                classification_response = cohere_client.classify(inputs=[input_text], examples=examples)
                category = classification_response['outputs'][0]['label']
                email['category'] = category
                classified_emails.append(email)
            except Exception as e:
                print("Error classifying email:", str(e))
        else:
            print("Empty email body detected, skipping classification.")
    return classified_emails

# Main function to fetch and classify emails
def main():
    # Start the Flask server in a subprocess
    server_process = subprocess.Popen(["python3", "gmail_api.py"])
    # Wait for a few seconds to allow the server to start
    time.sleep(5)
    
    emails = fetch_emails()
    if emails:
        classified_emails = classify_emails(emails)
        # Print or display the classified emails in the console
        for email in classified_emails:
            print("Email:", email['body'])
            print("Category:", email.get('category', 'Unclassified'))
            print("--------------------------------------")
    else:
        print("No emails fetched.")
    
    # Terminate the Flask server subprocess
    server_process.terminate()

if __name__ == "__main__":
    main()
