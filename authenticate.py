import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow

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
