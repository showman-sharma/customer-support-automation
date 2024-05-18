import base64
import json
import re
from feedback import feedbackcode
from mailauthcate import mailauthenticate
from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



def send_email(to_address, subject, classfi, body):
    creds = mailauthenticate()
    feedback_content = feedbackcode(subject, body, to_address, classfi)
    
    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content(feedback_content, subtype="html")
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
        return send_message
    except HttpError as error:
        print(f"An error occurred: {error}")
        
def forwardmessage(to_address, subject, body):
    creds = mailauthenticate()
    
    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()
        pattern = r'<([^>]+)>'
        matches = re.findall(pattern, to_address)
        if matches:
            sendermail = matches[0]
        messbody = body + "<br><br> This email was forwarded because it was unpredicatable." + "<br><br>" + "Sender Mail ID: " + to_address + "<br><br>" + "Sender Email: " + sendermail + "<br><br>" + "Subject: " + subject

        message.set_content(messbody, subtype="html")
        message["To"] = "testpixeltest8@gmail.com"
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
        return send_message
    except HttpError as error:
        print(f"An error occurred: {error}")
