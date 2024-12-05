# input_handler.py (Updated)

import speech_recognition as sr


def get_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Listening...")
    with mic as source:
        # This adjustment is key for noisy environments
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        # This printout is crucial for your tracking and improvement quantification
        print(f"I heard you say: '{text}'")
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand your voice."
    except sr.RequestError:
        return "Sorry, the speech recognition service is unavailable. (Check network)"


def get_text_input():
    return input("Enter your query : ")


def extract_topic_from_query(query):
    query = query.lower().strip()

    trigger_phrases = [
        "tell me about", "what is", "what are", "who is", "who was",
        "explain", "describe", "write an article about", "write about",
        "give me a summary of", "can you tell me about"
    ]

    for phrase in trigger_phrases:
        if query.startswith(phrase):
            query = query[len(phrase):].strip()
            break

    # Remove common articles like 'the', 'a', 'an' at the beginning
    if query.startswith(("the ", "a ", "an ","i","is","from")):
        query = query.split(" ", 1)[1]

    return query
