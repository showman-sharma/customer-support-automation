import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
import googleapiclient.errors
import logging
from googleapiclient.discovery import build

fetched_emails = []
latest_email_id = None
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
    except googleapiclient.errors.HttpError as e:
        logging.error("Gmail API HTTP error occurred: %s", e)
        return None
    except Exception as e:
        logging.error("An error occurred while fetching unread emails: %s", e)
        return None


def get_email(service, message_id):
    try:
        message = service.users().messages().get(userId='me', id=message_id['id']).execute()
        return message
    except Exception as e:
        print("An error occurred:", e)
        return None
    
def fetch_and_update_emails():
    global fetched_emails, latest_email_id
    try:
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds:
            logging.error("Authentication failed. Cannot fetch emails.")
            return
        
        service = build('gmail', 'v1', credentials=creds)
        message_ids = get_unseen_emails(service)
        new_emails = []

        if message_ids:
            for message_id in message_ids:
                if latest_email_id is None or message_id['id'] > latest_email_id:
                    if message_id['id'] not in fetched_emails:  # Check if email ID has been processed before
                       return message_id
        
        fetched_emails += new_emails
    except Exception as e:
        logging.error("An error occurred during email fetching and update: %s", e)
