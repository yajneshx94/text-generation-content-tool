import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Use voice 1 (Zira) or fallback to default
try:
    engine.setProperty('voice', voices[1].id)
except IndexError:
    engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 140)

def speak(text):
    engine.say(text)
    engine.runAndWait()
