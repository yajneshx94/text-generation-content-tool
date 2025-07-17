from input_handler import get_voice_input, get_text_input, extract_topic_from_query
from wiki_fetcher import get_wikipedia_summary
from text_generator import generate_text
from voice_output import speak


def main():
    print("AI Content Creator Initialized.")
    mode = input("Choose input method ('voice' or 'text'): ").strip().lower()
    print(f"Input mode selected: '{mode}'")

    if mode == "voice":
        print("\nPlease state what you want to learn about. ")
        query = get_voice_input()
    else:
        query = get_text_input()

    print(f"User query: '{query}'")

    # Handle recognition failure or service unavailability
    if "Sorry" in query or "unavailable" in query:
        print(query)
        speak(query)
        return

    # Extract the core topic
    topic = extract_topic_from_query(query)

    # Get Wikipedia summary
    wiki_summary = get_wikipedia_summary(topic)
    if "Sorry" in wiki_summary:
        print(wiki_summary)
        speak(wiki_summary)
        return

    print(" Now generating AI content...")

    # Prepare prompt for AI text generation
    prompt = (
        f"Based *only* on the following context, write a concise and informative summary about '{topic}'.\n\n"
        f"Context:\n{wiki_summary}\n\n"
        f"Summary (do NOT include references or citations):"
    )

    # Generate AI content
    ai_generated = generate_text(prompt)

    print("\nGenerated Content:\n" + ai_generated)
    speak(ai_generated)


if __name__ == "__main__":
    main()
