from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1", device_map="auto")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_answer(query):
    context = "\n".join(retrieve_docs(query))
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    return generator(prompt, max_new_tokens=150)[0]['generated_text']
