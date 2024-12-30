import re
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter

# File path and Reading data
file_path = "Data\PakistanConstituion\pdf_data.json"
df = pd.read_json(file_path)

def clean_text(text):
    # Remove newline characters and excessive spaces
    text = re.sub(r'\n', ' ', text)             # Replace newlines with spaces
    
    # Handle cases like "T H E   C H U R C H   O F   S C O T L A N D"
    # Match sequences of single letters separated by spaces and rejoin them
    text = re.sub(r'(?<=\b(?:[A-Za-z])) (?=(?:[A-Za-z]\b))', '', text)

    text = re.sub(r'[^\w\s]', '', text)         # Remove special characters except spaces
    text = re.sub(r'\s+', ' ', text)            # Replace multiple spaces with a single space
    return text.strip().lower()                 # Strip leading/trailing spaces and lowercase the text

# Cleaning to the 'text' column
df['cleaned_text'] = df['text'].apply(clean_text)

# Text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800, chunk_overlap=200,
    separators=["\n", ".", " "]
)

# Prepare chunks and ids
chunked_data = []

for _, row in df.iterrows():
    file_name = row['file_name']
    cleaned_text = row['cleaned_text']
    
    # Split text into chunks
    chunks = text_splitter.split_text(cleaned_text)
    
    # Prepare chunk data
    for idx, chunk in enumerate(chunks):
        chunk_id = f"{file_name}_chunk{idx + 1}"
        chunked_data.append({"id": chunk_id, "document": chunk})

# Convert to DataFrame
chunked_df = pd.DataFrame(chunked_data)

# Saving Chunked data
new_file_path = "Data/PakistanConstituion/chunked_data.csv"
chunked_df.to_csv(new_file_path, index=False)