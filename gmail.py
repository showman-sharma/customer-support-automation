import os
import base64
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    creds = None         
    access_token = None
    refresh_token = None

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

def main():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)

    message_ids = get_unseen_emails(service)

    if message_ids:
        for message_id in message_ids:
            message = get_email(service, message_id)
            if message:
                sender = next((header['value'] for header in message['payload']['headers'] if header['name'] == 'From'), '')
                subject = next((header['value'] for header in message['payload']['headers'] if header['name'] == 'Subject'), '')
                body = ''

                # Process message body
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
                
                json_data = json.dumps(email_data, indent=4)
                
                with open(f"email_{message_id['id']}.json", "w") as file:
                    file.write(json_data)
                
                print("New email received and processed.")

    print("Email retrieval and processing complete.")

if __name__ == '__main__':
    main()

   #  https://accounts.google.com/o/oauth2/auth?client_id=881685451226-6t0c6mo08u2kn5ap4alfqt59mquv06vn.apps.googleusercontent.com&redirect_uri=http://localhost&response_type=code&scope=https://www.googleapis.com/auth/gmail.readonly&access_type=offline

#   http://localhost/?code=4/0AeaYSHDMuR4kmYWkQEAPBqcpXwIujyZ6Cr09TgPxhp1Rd9-kiSDGi3WqRJHemmdGEDaULw&scope=https://www.googleapis.com/auth/gmail.readonly
  #   // curl --request POST --data "code= 4/0AeaYSHDMuR4kmYWkQEAPBqcpXwIujyZ6Cr09TgPxhp1Rd9-kiSDGi3WqRJHemmdGEDaULw&client_id= 881685451226-6t0c6mo08u2kn5ap4alfqt59mquv06vn.apps.googleusercontent.com&client_secret=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&redirect_uri=http://- localhost&grant_type=authorization_code" https://oauth2.googleapis.com/token