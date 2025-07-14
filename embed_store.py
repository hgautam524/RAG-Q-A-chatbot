from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from load_dataset import documents  # ✅ Make sure this is here

# ✅ Load the documents from dataset


# ✅ Load embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# ✅ Generate embeddings
doc_embeddings = embedder.encode(documents)

# ✅ Build FAISS index
index = faiss.IndexFlatL2(doc_embeddings[0].shape[0])
index.add(np.array(doc_embeddings))

# ✅ Save index and documents
faiss.write_index(index, "faiss_index.idx")
with open("documents.npy", "wb") as f:
    np.save(f, np.array(documents))
