import urllib.parse
from message import code

def feedbacksolvedurl(subject,body,sender):
    encoded_body = urllib.parse.quote(body)
    encoded_subject = urllib.parse.quote(subject)
    encoded_sender = urllib.parse.quote(sender)
    
    url = f"https://praveentech21.github.io/supportpixceltest/solved.html?some=something&body={encoded_body}&sender={encoded_sender}&subject={encoded_subject}"
    return url

def feedbackunsolvedurl(subject,body,sender):
    encoded_body = urllib.parse.quote(body)
    encoded_subject = urllib.parse.quote(subject)
    encoded_sender = urllib.parse.quote(sender)
    
    url = f"https://praveentech21.github.io/supportpixceltest/unsolved.html?some=something&body={encoded_body}&sender={encoded_sender}&subject={encoded_subject}"
    return url

def feedbackcode(subject,body,sender,classfi):
    solvedurl = feedbacksolvedurl(subject,body,sender)
    unsolvedurl = feedbackunsolvedurl(subject,body,sender)
    formated_response = code(solvedurl,unsolvedurl,classfi)
    
    return formated_response