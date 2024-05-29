from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
CORS(app)

# Replace the following with your MongoDB connection string
client = MongoClient('mongodb://localhost:27017/genaration')
db = client['genaration']
issues_collection = db['genaration']

def generate_ticket_id():
    last_issue = issues_collection.find_one(sort=[('_id', -1)])
    if last_issue:
        last_ticket_id = last_issue.get('ticket_id', 0)
        return last_ticket_id + 1
    else:
        return 1

@app.route('/issues', methods=['GET'])
def get_issues():
    issues = list(issues_collection.find())
    for issue in issues:
        issue['_id'] = str(issue['_id'])
    return jsonify(issues)

@app.route('/submit', methods=['POST'])
def submit_issue():
    data = request.json
    email = data['email']
    issue_text = data['issue']
    ticket_id = generate_ticket_id()
    issues_collection.insert_one({'ticket_id': ticket_id, 'email': email, 'issue': issue_text, 'status': 'open'})
    return jsonify({'message': 'Issue submitted successfully'})

@app.route('/solve/<issue_id>', methods=['POST'])
def solve_issue(issue_id):
    issues_collection.update_one({'_id': ObjectId(issue_id)}, {'$set': {'status': 'closed'}})
    return jsonify({'message': 'Issue marked as solved'})

@app.route('/unsolve/<issue_id>', methods=['POST'])
def unsolve_issue(issue_id):
    issues_collection.update_one({'_id': ObjectId(issue_id)}, {'$set': {'status': 'open'}})
    return jsonify({'message': 'Issue marked as unsolved'})

if __name__ == '__main__':
    app.run(debug=True)
