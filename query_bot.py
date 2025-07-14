import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from model_utils import generate_hf_answer  # ✅ Hugging Face only

# Load FAISS index and documents
index = faiss.read_index("faiss_index.idx")
documents = np.load("documents.npy", allow_pickle=True).tolist()

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_docs(query, top_k=3):
    query_embedding = embedder.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)
    return [documents[i] for i in I[0]]

def generate_answer(query):  # ✅ Use only HF version
    context = "\n".join(retrieve_docs(query))
    return generate_hf_answer(context, query)
