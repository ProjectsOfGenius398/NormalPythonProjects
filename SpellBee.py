import random
import pyttsx3
from spellchecker import SpellChecker

spellBee = ["terracotta", "unsettling", "jostling", "shemozzle", "audacity", "concentration", "doubly", "fallacy", "despite", "maniac", "sprung", "wandering", "sustenance", "subtle", "miniature", "perplexed", "sustenance", "liaison", "spasm", "boundless", "breathes", "invariably", "grimacing", "drudgery", "equinox", "clenched", "whence", "strand", "well-tended", "collided", "patriarch", "winced", "squander", "forfeit", "sheriff"]

engine = pyttsx3.init()
spell = SpellChecker()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

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
        attempts = 0
        while True:
            user_input = input("Enter the spelling of the word: ")
            if user_input.lower() == "repeat":
                engine.say(word)
                engine.runAndWait()
                continue
            correct_spelling = spell.correction(user_input)
            if user_input != word:
                attempts += 1
                if attempts < 3:
                    print(f"Incorrect, try again or enter 'repeat' to hear the word again")
                    continue
                else:
                    print(f"Incorrect, the correct spelling is {word}")
                    wrong[user_input] = word
                    wordsstuff.append(user_input)
            else:
                print("Correct!")
                score=score+1
                print("You have spelt ",score," out of 35 words correctly!")
            break

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
            print("Awesome!")

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
