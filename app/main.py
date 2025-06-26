from input_handler import get_voice_input, get_text_input
from wiki_fetcher import get_wikipedia_summary
from text_generator import generate_text
from voice_output import speak

def main():
    print("AI Content Creator")
    mode = input("Choose input type ('voice' or 'text'): ").strip().lower()

    topic = get_voice_input() if mode == "voice" else get_text_input()

    wiki_summary = get_wikipedia_summary(topic)
    if "Sorry" in wiki_summary:
        speak(wiki_summary)
        return
    else:
        prompt = (
            f"Write a detailed, informative article about {topic} in 100 words. Here's the Content:\n\n"
            f"{wiki_summary}\n\n"
            "Keep the language simple and interesting for beginners."
        )
        ai_generated = generate_text(prompt)

        # this is where our pyttsx3 produce speech outputtext

        print(f"\nThe Generated Content:\n{ai_generated}\n")
        speak(ai_generated)

if __name__ == "__main__":
    main()
