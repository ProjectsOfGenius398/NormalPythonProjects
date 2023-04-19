import random
import pyttsx3
from spellchecker import SpellChecker

spellBee = ["ambiguous", "unsettling", "shemozzle", "audacity", "etiquette", "demeanor", "jostling", "facsimile", "despite", "turbulence", "subsequent", "souvenir", "foreign", "whence", "miniature", "perplexed", "insouciant", "acquaintance", "boundless", "haphazard", "despair", "invariably", "judicious", "sumptuous", "clenched", "fortitude", "endeavor", "pelf", "hindrance", "retrieve", "unflinching", "patriarch", "forfeit", "accumulate", "unsung"]

engine = pyttsx3.init()
spell = SpellChecker()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

already_said = set()
score=0
wrong = {}
wordsstuff=[]
while True:
    word = random.choice(spellBee)
    if word not in already_said:
        already_said.add(word)
        engine.say(word)
        engine.runAndWait()
        user_input = input("Enter the spelling of the word: ")
        correct_spelling = spell.correction(user_input)
        if user_input != word:
            print(f"Incorrect, the correct spelling is {word}")
            wrong[user_input] = word
            wordsstuff.append(user_input)
        else:
            print("Correct!")
            score=score+1
            print("You have spelt ",score," out of 35 words correctly!")

    if len(already_said) == len(spellBee):
        print("All words have been said.")
        length=len(wordsstuff)
        length1=len(spellBee)
        length2=length1-length
        if score<=5:
            print("You can do this! Just a bit more effort")
        elif score <=15 and score >=5:
            print("You are on the right track!")
        elif score <=25 and score >=15:
            print("Just a bit more to go!")
        elif score <=30 and score >=25:
            print("So close!")
        elif score <=35 and score >=30:
            print("A bit more! C'mon!")
        elif score == 35:
            print("Perfection lad! Pure, undisturbed perfection")

        print("\nYou got ",length," words wrong and ",length2," words correctly. They have been saved into a txt file.")
        with open("misspelled_words.txt", "w") as f:
            for k, v in wrong.items():
                f.write(f"{k} -> {v}\n")
                print(f"{k} -> {v}")

        option=input("\n Do you want to try again? (y/n)").lower()
        if option=="y":
            # Repeat the spell bee only for the words that were spelled incorrectly
            spellBee = list(wrong.values())
            already_said = set()
            wrong = {}
            wordsstuff = []
        else:
            break
