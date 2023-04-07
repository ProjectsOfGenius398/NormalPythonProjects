import random
import numpy as np

# Get user input for lowest number, highest number, and number of questions
LowestNumberRange = int(input("Please enter the lowest number you want to get the questions from: "))
HighestNumberRange = int(input("Please enter the highest number you want to get the questions from: "))   
QuestionsNumber = int(input("How many questions do you want? "))  

# Generate questions and answers
QuestionArray = []  
for i in range(QuestionsNumber):
    # Generate two random numbers for the base and exponent
    base1 = random.randint(LowestNumberRange, HighestNumberRange)
    exponent1 = random.randint(1, 5)

    base2 = random.randint(LowestNumberRange, HighestNumberRange)
    exponent2 = random.randint(1, 5)    

    # Generate a random operator
    operators = ["+", "-", "*", "/"]
    operator = random.choice(operators)

    # Generate a random question
    if operator == "+":
        question = f"What is the value of {base1}^{exponent1} + {base2}^{exponent2}?"
        answer = base1**exponent1 + base2**exponent2
    elif operator == "*":
        question = f"What is the value of {base1}^{exponent1} * {base2}^{exponent2}?"
        answer = base1**exponent1 * base2**exponent2
    elif operator == "/":
        question = f"What is the value of {base1}^{exponent1} / {base2}^{exponent2}?"
        answer = base1**exponent1 / base2**exponent2
    else:
        question = f"What is the value of {base1}^{exponent1} - {base2}^{exponent2}?"
        answer = base1**exponent1 - base2**exponent2

    QuestionArray.append((question, answer))

# Get user input for solving or downloading questions
choice = input("Do you want to solve the questions now? (y/n): ")
if choice == 'y':
    # Print questions and get user input for answers
    score = 0
    for i, (question, correct_answer) in enumerate(QuestionArray):
        print(f"\nQuestion {i+1}: {question}")
        user_answer = input("Answer: ")
        try:
            user_answer = float(user_answer)
            if np.isclose(user_answer, correct_answer):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {correct_answer}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Print final score
    print(f"\nYour final score is {score} out of {QuestionsNumber}")
else:
    # Write questions and answers to a text file
    with open("questions.txt", "w") as f:
        for question, answer in QuestionArray:
            f.write(f"{question}\nAnswer: {answer}\n\n")
    print("Questions saved to file.")
