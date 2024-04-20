import json
import cohere
from cohere.responses.classify import Example

def classify_emails(email_body):
    co = cohere.Client('ue55vlS7fa5BCJ9FgrPi3814EBfMg1UvIihFNbzo')
    
    with open('category.json', 'r') as file:
        examples_data = json.load(file)
        
    examples = [Example(example['message'], example['label']) for example in examples_data['examples']]

    # Classify each email
    if email_body:
        classification_response = co.classify(
            inputs=[email_body],  
            examples=examples,
        )
        
        classification = classification_response[0]
        predition = classification.prediction
        confidence = classification.confidence

    return predition, confidence
