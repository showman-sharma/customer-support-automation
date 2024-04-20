import os
import webbrowser
from threading import Thread
from flask import Flask, request

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

mailapp = Flask(__name__)

def mailauthenticate():
    authenticate()
    creds = None

    if os.path.exists('mailtoken.json'):
        creds = Credentials.from_authorized_user_file('mailtoken.json', SCOPES)
        
    return creds

def authenticate():
    creds = None         

    if os.path.exists('mailtoken.json'):
        creds = Credentials.from_authorized_user_file('mailtoken.json', SCOPES)
        
    if not creds or not creds.valid:
        flow = Flow.from_client_secrets_file(
            'credentials.json',  # Path to your client secret JSON file
            scopes=SCOPES,
            redirect_uri='http://localhost:8000/callback'
        )
        auth_url, _ = flow.authorization_url(prompt='consent')

        # Open the auth URL in the default web browser automatically
        webbrowser.open(auth_url)

        server = Thread(target=mailapp.run, kwargs={'port': 8000})
        server.start()

    return creds

@mailapp.route('/callback')
def google_auth_callback():
    auth_code = request.args.get('code')
    flow = Flow.from_client_secrets_file('credentials.json', scopes=SCOPES, redirect_uri='http://localhost:8000/callback')
    flow.fetch_token(code=auth_code)
    creds = flow.credentials
    with open('mailtoken.json', 'w') as token:
        token.write(creds.to_json())
    return 'Token Created Successfully'

