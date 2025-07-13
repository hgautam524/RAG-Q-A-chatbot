from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedder = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = embedder.encode(documents)

# Create FAISS index
index = faiss.IndexFlatL2(doc_embeddings[0].shape[0])
index.add(np.array(doc_embeddings))

