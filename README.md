# 💬 RAG Loan Q&A Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using Hugging Face models and a real-world loan approval dataset. It retrieves relevant examples from a dataset using semantic search (FAISS) and generates intelligent answers using a lightweight LLM like FLAN-T5. No OpenAI key required — fully local, free, and private.

---

## 📌 Features

- 🔍 Document retrieval from tabular CSV data (Loan Approval Dataset)
- 🧠 Context-aware Q&A using Hugging Face models (e.g., `flan-t5-small`)
- 💬 Simple Streamlit UI for interactive questions
- 💾 FAISS vector database for fast local similarity search
- ✅ No API required — works offline using local models

---

## 🛠 Tech Stack

| Layer           | Technology                          |
|----------------|--------------------------------------|
| Embedding       | `sentence-transformers (MiniLM)`     |
| Vector DB       | `FAISS`                              |
| LLM (Generation)| `Hugging Face Transformers`          |
| UI              | `Streamlit`                          |
| Dataset         | [Loan Approval Prediction Dataset](https://www.kaggle.com/datasets/sonalisingh1411/loan-approval-prediction) |

---

## 📁 Project Structure

<img width="709" height="386" alt="image" src="https://github.com/user-attachments/assets/9e475e34-c915-45b9-922d-62e9c1831c28" />


---

## 🧠 How It Works

1. The dataset is split into readable row-level document chunks.
2. These chunks are embedded using `MiniLM` and indexed in FAISS.
3. On user query:
   - Top relevant examples are retrieved from FAISS.
   - The query + context are passed to a Hugging Face model (like FLAN-T5).
   - The model generates an intelligent answer based on context.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rag-qna-chatbot.git
cd rag-qna-chatbot
```

### 2. Create a Virtual Environment (optional but recommended)
```bash

python -m venv venv
# Activate it
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
```
### 3. Install Dependencies
```bash

pip install -r requirements.txt
```
### 4. Download the Dataset (if not included)
Download Training Dataset.csv from:
🔗 Loan Approval Prediction Dataset

Place it in the root of the project folder.

### 5. Generate Embeddings & FAISS Index (Run Once)
```bash

python embed_store.py
```
This will:

- Process the dataset

- Create embeddings

- Save a FAISS index (faiss_index.idx)

- Save the documents (documents.npy)

### 6. Run the Chatbot App
```bash

streamlit run app.py
```
A browser window will open with a user interface where you can ask questions like:

- "What happens if an applicant has no credit history?"

- "How does being self-employed affect loan approval?"

## 🧠 Example Output
```pgsql

**Question:** Does high income guarantee loan approval?

**Answer:** Even applicants with high income may be denied if they have poor credit history or inconsistent employment. Loan approval depends on multiple factors like credit history, employment status, and loan term.
```

## ✅ Requirements
```text

streamlit
pandas
numpy
faiss-cpu
sentence-transformers
transformers
torch
```
## 📌 To-Do (Optional Features)
 - Add OpenAI/Gemini model toggle

 - Upload support for PDF/CSV files

 - Add chatbot memory/history

 - Deploy to Hugging Face Spaces / Streamlit Cloud

## 📜 License
This project is for educational purposes. Attribution required if reused.

## 🤝 Contributing
PRs are welcome! If you have suggestions or want to add features, feel free to open an issue or submit a pull request.

## 👤 Author
Built by Himanshu Gautam
- 📧 hgautam524@gmail.com
- 🔗 GitHub: [https](https://github.com/hgautam524)

