# text_generator.py
import os
import torch
from transformers import pipeline

# Disable symlink warning
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# Using TinyLlama 1.1B chat model from hugging face
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

device = 0 if torch.cuda.is_available() else -1

generator = pipeline(
    "text-generation",
    model=MODEL_NAME,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device=device,
)

def generate_text(prompt, max_len=256):
    print("Generating content with TinyLlama 1.1B...")

    outputs = generator(
        prompt,
        max_length=max_len,
        num_return_sequences=1,
        truncation=True,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    full_text = outputs[0]["generated_text"]
    print("\n[DEBUG] Full output from model:\n", full_text)

    # Clean the output by removing prompt from the start
    new_content = full_text[len(prompt):].strip()

    # Additional cleanup if model echoes instruction-like format
    marker = "Summary (do NOT include references or citations):"
    if marker in new_content:
        summary_start = new_content.find(marker) + len(marker)
        new_content = new_content[summary_start:].strip()

    if not new_content:
        return "⚠️ AI did not return new content. Try again with a simpler or different topic."

    print("\nGenerated Content:\n", new_content)
    return new_content
