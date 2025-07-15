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

