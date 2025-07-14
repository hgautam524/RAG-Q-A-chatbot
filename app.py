import streamlit as st
from query_bot import generate_answer  # ✅ Required import

st.title("Loan Approval Q&A Chatbot 💬")

user_query = st.text_input("Ask something about loan approvals...")

if user_query:
    with st.spinner("Generating response..."):
        answer = generate_answer(user_query)
        st.write("**Answer:**", answer)
