from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

def generate_answer(question, context):
    input_text = f"question: {question}  context: {context}"
    inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True)
    outputs = model.generate(inputs, max_length=150)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer