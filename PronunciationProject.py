import random
import pyttsx3
from spellchecker import SpellChecker

spellBee = ["ambiguous", "unsettling", "shemozzle", "audacity", "etiquette", "demeanor", "jostling", "facsimile", "despite", "turbulence", "subsequent", "souvenir", "foreign", "whence", "miniature", "perplexed", "insouciant", "acquaintance", "boundless", "haphazard", "despair", "invariably", "judicious", "sumptuous", "clenched", "fortitude", "endeavor", "pelf", "hindrance", "retrieve", "unflinching", "patriarch", "forfeit", "accumulate", "unsung"]

engine = pyttsx3.init()
spell = SpellChecker()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'english-us')

already_said = set()
score=0
while True:
    word = random.choice(spellBee)
    if word not in already_said:
        already_said.add(word)
        engine.say(word)
        engine.runAndWait()
        user_input = input("Enter the spelling of the word: ")
        correct_spelling = spell.correction(user_input)
        while user_input != word:
            print(f"Incorrect, the correct spelling is {word}")
            user_input = input("Enter the spelling of the word: ")
            correct_spelling = spell.correction(user_input)
        print("Correct!")
        score=score+1
        print("You have spelt ",score," out of 35 words correctly!")

    if len(already_said) == len(spellBee):
        print("All words have been said.")
        print("Your score is ", score, "! Great job!")
        break