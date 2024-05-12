from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import pandas as pd
from pymongo import MongoClient
import os
import logging

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for CSRF protection

# Define MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['email_data']
collection = db['email']

# Define Excel file path
excel_file = 'sample_data.xlsx'

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Validate email address
def is_valid_email(email):
    # Implement email validation logic here (e.g., using regex)
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Validate form data
        name = request.form.get('name')
        email = request.form.get('email')
        if not name or not email:
            raise ValueError("Name and email are required")
        if not is_valid_email(email):
            raise ValueError("Invalid email address")

        # Write data to Excel file
        df = pd.DataFrame({'Name': [name], 'Email': [email]})
        df.to_excel(excel_file, mode='a', index=False, header=not os.path.exists(excel_file))

        # Insert data into MongoDB
        data = {'name': name, 'email': email}
        collection.insert_one(data)

        flash('Data submitted successfully!', 'success')
        logging.info('Data submitted successfully: Name=%s, Email=%s', name, email)
        return redirect(url_for('index'))
    except Exception as e:
        flash('An error occurred while processing your request.', 'error')
        logging.error('Error processing request: %s', str(e))
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

