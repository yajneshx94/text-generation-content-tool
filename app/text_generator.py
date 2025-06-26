from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate_text(prompt, max_len=400):
    print(" Generating creative content...")
    result = generator(prompt, max_length=max_len, num_return_sequences=1,truncation=True,pad_token_id=50256)
    return result[0]["generated_text"]
