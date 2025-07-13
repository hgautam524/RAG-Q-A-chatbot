import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import openai

# Load index and documents
index = faiss.read_index("faiss_index.idx")
documents = np.load("documents.npy", allow_pickle=True).tolist()

embedder = SentenceTransformer('all-MiniLM-L6-v2')
openai.api_key = "YOUR_OPENAI_API_KEY"  # replace this securely

def retrieve_docs(query, top_k=3):
    query_embedding = embedder.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)
    return [documents[i] for i in I[0]]

def generate_answer(query):
    context = "\n".join(retrieve_docs(query))
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
