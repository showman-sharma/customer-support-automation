import base64
import json
from authenticate import *
from send_resopnce import send_email, forwardmessage
from email_classifier import classify_emails
from flask import Flask, redirect, request, Response
from googleapiclient.discovery import build
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

@app.route('/')
def index():
    creds = None         

    if os.path.exists('token.json'):
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

    return redirect('/emails')

@app.route('/emails')
def fetch_emails():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('gmail', 'v1', credentials=creds)

    sample = fetch_and_update_emails()
        # Check if the sample is in send_mails.json
    with open('send_mails.json', 'r+') as file:
        data = json.load(file)
        sent_emails = [mail["id"] for mail in data["mails"]]
        if sample['id'] in sent_emails:
            print("No new Mails Recived.")
            return "No new Mails Recived."
        else:
            if sample:
                message = get_email(service, sample)
                if message:
                    sender = next((header['value'] for header in message['payload']['headers'] if header['name'] == 'From'), '')
                    subject = next((header['value'] for header in message['payload']['headers'] if header['name'] == 'Subject'), '')
                    body = ''

                    if 'parts' in message['payload']:
                        for part in message['payload']['parts']:
                            if part['mimeType'] == 'text/plain':
                                body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                                break

                    prediction, confidence = classify_emails(body) 
                    # logic to send mail directly 
                    if confidence < 0.65:
                        email_sent = forwardmessage(sender, subject, body)
                        if email_sent:
                            # Append the sample message ID to send_mails.json
                            data["mails"].append(sample)
                            file.seek(0)
                            json.dump(data, file, indent=4)
                            file.truncate()
                            print("Email Forwarded since it unpredicatable. ID appended to send_mails.json.")
                        return email_sent
                    else:
                        email_sent = send_email(sender, subject, prediction, body)  
                        if email_sent:
                            # Append the sample message ID to send_mails.json
                            data["mails"].append(sample)
                            file.seek(0)
                            json.dump(data, file, indent=4)
                            file.truncate()
                            print("Email sent and ID appended to send_mails.json.")
                        return email_sent
            else:
                return "No new emails found."

scheduler = BackgroundScheduler()
scheduler.add_job(fetch_emails, 'interval', seconds=5)
scheduler.start()

if __name__ == '__main__':
    app.run(port=5000)