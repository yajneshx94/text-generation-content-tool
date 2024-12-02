import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# the index 1 will Set voice to Microsoft Zira
engine.setProperty('voice', voices[1].id)

# Slow down the speech rate (default is usually ~200)
engine.setProperty('rate', 130)  # Lower value = slower speech

def speak(text):
    # Remove any prompts or unnecessary lines
    cleaned_text = text.strip().split("\n")[-1]  # Get last relevant line
    print(f" Speaking: {cleaned_text[:100]}...")
    engine.say(cleaned_text)
    engine.runAndWait()
