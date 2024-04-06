from flask import Flask, jsonify
from flask_cors import CORS
import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

app = Flask(__name__)
CORS(app)

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:        
            token.write(creds.to_json())

    return creds

def get_unseen_emails(service):     
    try:  
        messages = service.users().messages().list(userId='me', labelIds=['UNREAD']).execute()
        message_ids = messages.get('messages', [])
        return message_ids
    except Exception as e:
        print("An error occurred:", e)
        return None

def get_email(service, message_id):
    try:
        message = service.users().messages().get(userId='me', id=message_id['id']).execute()
        return message
    except Exception as e:
        print("An error occurred:", e)
        return None

@app.route('/fetch_emails', methods=['GET'])
def fetch_emails():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)
    message_ids = get_unseen_emails(service)
    emails = []

    if message_ids:
        for message_id in message_ids:
            message= get_email(service, message_id)
            if message:
                sender = next((header['value'] for header in message['payload']['headers'] if header['name'] == 'From'), '')
                subject = next((header['value'] for header in message['payload']['headers'] if header['name'] == 'Subject'), '')
                body = ''
                
                if 'parts' in message['payload']:
                    for part in message['payload']['parts']:
                        if part['mimeType'] == 'text/plain':
                            body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                            break  

                email_data = {
                    "sender": sender,
                    "subject": subject,
                    "body": body
                }
                emails.append(email_data)

    return jsonify(emails)

if __name__ == '__main__':
    app.run(debug=True)
