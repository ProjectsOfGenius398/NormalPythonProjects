english_words = ["help", "shopping", "despite", "otherwise", "washing clothes", "yesterday", "never", "now", "to fill", "vacuum cleaner", "to want", "to know", "often", "sensible", "hungry", "worst", "to understand", "how many", "during", "washing utensils", "rabbit", "shout", "to hear", "farewell"]
french_words = ["aider", "les courses", "malgre", "sinon", "la lessive", "hier", "jamais", "maintenant", "remplir", "aspirateur", "vouloir", "connaitre", "souvent", "prudent", "faim", "pire", "comprendre", "combien de", "pendant", "la vaisselle", "lapin", "crier", "entendre", "adieu"]
score=0
for i in range(len(english_words)):
    question = "What is the French word for " + english_words[i] + "?"
    answer = french_words[i]
    print(question)
    your_answer = input()
    if your_answer == answer:
        print("Correct!")
        score=score+1
    else:
        print("Incorrect. The answer is " + answer)
    print("You scored ", score, " out of 20")
