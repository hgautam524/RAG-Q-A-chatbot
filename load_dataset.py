import pandas as pd

df = pd.read_csv("C:\\Users\\Admin\\RAG-Q-A-chatbot\\Training Dataset.csv")
df.fillna("Unknown", inplace=True)

# Create doc-style text for each row
documents = []
for i, row in df.iterrows():
    doc = f"Applicant: {row['Gender']}, {row['Married']}, {row['Education']}, {row['Self_Employed']}.\n"
    doc += f"Income: {row['ApplicantIncome']}, Loan Amount: {row['LoanAmount']}, Term: {row['Loan_Amount_Term']}.\n"
    doc += f"Credit History: {row['Credit_History']}, Status: {row['Loan_Status']}"
    documents.append(doc)
