import random
import pyttsx3
from spellchecker import SpellChecker

spellBee = ["Diurnal", "Poignant", "Ablution", "Animosity", "Maneuver", "Incessant", "Homogenize", "Impasse",            "Distinction", "Labyrinth", "Pittance", "Facsimile", "Citadel", "Idiopathic", "Scorned", "Robust",            "Potpourri", "Tantalize", "Mercantile", "Fictitious", "Incandescent", "Uncouth", "Martyr",            "Pediatrician", "Hindsight", "Irreconcilable", "Palatable", "Consciousness", "Acquiesce",            "Picturesque", "Chastise", "Indelible", "Blasphemous", "Derelict", "Pandemonium"]

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