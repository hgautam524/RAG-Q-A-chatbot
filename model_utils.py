from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Hugging Face model
HF_MODEL = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(HF_MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(HF_MODEL)

qa_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_hf_answer(context: str, query: str) -> str:
    prompt = f"Answer the question based on the context.\n\nContext: {context}\n\nQuestion: {query}"
    result = qa_pipeline(prompt, max_new_tokens=150)
    return result[0]["generated_text"]
