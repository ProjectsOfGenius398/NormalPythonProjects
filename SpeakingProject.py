import pyttsx3
engine = pyttsx3.init()

word = input("Please enter a word to pronounce: ")

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.8)

engine.say(word)
engine.runAndWait()