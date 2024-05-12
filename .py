import pandas as pd

# Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Specify the file name
excel_file = 'sample_data.xlsx'

# Write DataFrame to Excel file
df.to_excel(excel_file, index=False)

print(f"Excel file '{excel_file}' created successfully with sample data.")
