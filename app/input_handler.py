import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print(" Listening... Speak your topic.")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f" You said: {text}")
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand your voice."
    except sr.RequestError:
        return "Speech recognition service is unavailable."

def get_text_input():
    return input(" Enter your topic: ")
