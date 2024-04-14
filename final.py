import os
import base64
import json
from flask import Flask, redirect, request, Response, jsonify

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    creds = None         

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    if not creds or not creds.valid:
        flow = Flow.from_client_secrets_file(
            'credentials.json',  # Path to your client secret JSON file
            scopes=SCOPES,
            redirect_uri='http://localhost:5000/callback'
        )
        authorization_url, _ = flow.authorization_url(prompt='consent')
        return authorization_url, flow
    else:
        return None, None

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

@app.route('/')
def index():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if creds and creds.valid:
        return redirect('/emails')
    else:
        authorization_url, flow = authenticate()
        return redirect(authorization_url)


@app.route('/callback')
def callback():
    code = request.args.get('code')
    flow = Flow.from_client_secrets_file(
        'credentials.json',
        scopes=SCOPES,
        redirect_uri='http://localhost:5000/callback'
    )
    flow.fetch_token(code=code)
    creds = flow.credentials

    with open('token.json', 'w') as token:        
        token.write(creds.to_json())

    return 'Authorization successful. You can now close this window.'

@app.route('/emails')
def fetch_emails():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('gmail', 'v1', credentials=creds)

    message_ids = get_unseen_emails(service)
    all_emails = []

    if message_ids:
        def generate_emails():
            for message_id in message_ids:
                message = get_email(service, message_id)
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
                        message_id['id'] : {
                            "sender": sender,
                            "subject": subject,
                            "body": body
                        }
                    }
                    all_emails.append(email_data)
                    yield f"New email received and processed: {subject}\n"   
                    
                    print("New email received and processed.")
            
            with open("all_emails.json", "w") as file:
                json.dump(all_emails, file, indent=4)
                
        return Response(generate_emails(), content_type='text/plain')
                
    return jsonify(all_emails)

if __name__ == '__main__':
    app.run(port=5000)
