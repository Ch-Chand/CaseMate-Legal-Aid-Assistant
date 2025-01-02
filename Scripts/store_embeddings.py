import chromadb
import pandas as pd
from tqdm import tqdm

# Reading file
file_path = "../Data/PakistanConstituion/chunked_data.csv"
df = pd.read_csv(file_path)


# Creating Client
client = chromadb.PersistentClient(path="chroma_db")

# Creating collection
collection = client.get_or_create_collection(
    name="constitutes_docs"
)

# Maximum batch size allowed by ChromaDB
MAX_BATCH_SIZE = 5461

# Split the data into smaller batches
for i in tqdm(range(0, len(df), MAX_BATCH_SIZE)):
    batch = df.iloc[i:i + MAX_BATCH_SIZE]
    
    # Add each batch to the ChromaDB collection
    collection.add(
        documents=batch.document.to_list(),
        ids=batch.id.to_list(),
    )

print("Data added to ChromaDB successfully in batches.")
