import wikipedia

def get_wikipedia_summary(topic):
    try:
        summary = wikipedia.summary(topic, sentences=2)
        print(f"\n Wikipedia Summary:\n{summary}\n")
        return summary
    except Exception as e:
        print(f" Error: {e}")
        return "Sorry, I couldn't find that on Wikipedia."
