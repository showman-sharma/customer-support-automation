import base64
import os
import json

from feedback_form import response_form_mail
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate():
    creds = None
    
    if os.path.exists('mailtoken.json'):
        creds = Credentials.from_authorized_user_file('mailtoken.json', SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('mailtoken.json', 'w') as token:        
            token.write(creds.to_json())

    return creds

def get_emails():
    with open('email_classes.json') as f:
        emails_data = json.load(f)
    return emails_data['mails']

def get_responses():
    with open('responce_mails.json') as f:
        responses_data = json.load(f)
    return responses_data['responces']

def send_email(to_address, subject, response_content):
    creds = authenticate()
    
    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()
        

        message.set_content(response_content)
        message.add_alternative(response_form_mail, subtype='html')
        message["To"] = to_address
        message["From"] = "testpixeltest8@gmail.com"
        message["Subject"] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")

def process_emails():
    emails = get_emails()
    responses = get_responses()
    
    for mail, data in emails.items():
        to_address = data['from']
        subject = data['subject']
        classfi = data['classfi']
        response_content = responses.get(classfi, {}).get('responce', 'Default response')
        
        send_email(to_address, subject, response_content)

if __name__ == "__main__":
    process_emails()
