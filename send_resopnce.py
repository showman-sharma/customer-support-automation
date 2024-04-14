import base64
import os
import json
from google_auth_oauthlib.flow import Flow
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from flask import Flask, redirect, request, Response, jsonify

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
            flow = Flow.from_client_secrets_file(
            'credentials.json',  # Path to your client secret JSON file
            scopes=SCOPES,
            redirect_uri='http://localhost:5000/callback')
            authorization_url, _ = flow.authorization_url(prompt='consent')
            
        
        with open('mailtoken.json', 'w') as token:        
            token.write(creds.to_json())

    return creds

def get_responses():
    with open('responce_mails.json') as f:
        responses_data = json.load(f)
    return responses_data['responces']

def get_responce(classfi):
    responses = get_responses()
    response_content = responses.get(classfi, {}).get('responce', 'Default response')
    return response_content

def send_email(to_address, subject, classfi):
    creds = authenticate()
    response_content = get_responce(classfi)
    
    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content(response_content)
        message["To"] = to_address
        message["From"] = "testpixeltest8@gmail.com"
        message["Subject"] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")
        


if __name__ == "__main__":
    send_email("to_address", "subject", "response_content")
