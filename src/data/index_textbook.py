from langchain.document_loaders import PyPDFLoader
import requests
import pandas as pd
import pickle

# Load the PDF
loader = PyPDFLoader("data/raw/Chemistry2e-WEB.pdf")
pages = loader.load_and_split()

# Hugging Face model and token
model_id = "sentence-transformers/all-MiniLM-L6-v2"
hf_token = "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"
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}

# Function to query the API
def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options": {"wait_for_model": True}})
    return response.json()

# query each page and store embeddings
page_embeddings = {}

for i, page in enumerate(pages):
    print(f"Processing page {i+1}/{len(pages)}")
    page_content = page.page_content
    embeddings = query(page_content)
    page_embeddings[f'page_{i+1}'] = embeddings

# Save all embeddings
with open('all_embeddings.pkl', 'wb') as file:
    pickle.dump(page_embeddings, file)





