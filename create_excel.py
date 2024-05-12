import pandas as pd
from pymongo import MongoClient

# Read Excel file
excel_file = 'sample_data.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['email_data']  # Replace with your database name
collection = db['email']  # Replace with your collection name

# Insert data into MongoDB
for index, row in df.iterrows():
    data_dict = row.to_dict()
    collection.insert_one(data_dict)

print("Data inserted into MongoDB collection.")
