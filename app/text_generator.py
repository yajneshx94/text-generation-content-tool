#text_generator.py
def generate_text(topic, wiki_summary, max_len=150):
    prompt = (
        f"Based *only* on the following context, write a concise and informative summary about '{topic}'.\n\n"
        f"Context:\n{wiki_summary}\n\n"
        f"Summary (do NOT include references or citations):"
    )

    try:
        output = generator(
            prompt,
            max_length=max_len,
            do_sample=True,
            pad_token_id=generator.tokenizer.eos_token_id,
            num_return_sequences=1,
            temperature=0.7,
            top_k=50,
        )
        generated = output[0]["generated_text"]

        # 🧼 Remove prompt part from generated output
        # Keep only the part that follows the last colon (:) in prompt
        split_output = generated.split("Summary (do NOT include references or citations):")
        if len(split_output) > 1:
            return split_output[1].strip()
        else:
            return generated.strip()

    except Exception as e:
        return "⚠️ Error generating content. Please try again."
