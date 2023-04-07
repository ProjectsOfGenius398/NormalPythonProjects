print("Rock, Paper, Scissors Game")
import time

def wait(seconds):
    time.sleep(seconds)

while True:
    print("Enter choice \n1 for Rock \n2 for Paper \n3 for Scissors")
    
    choice = int(input("Your turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("Invalid input. Please enter a valid option: "))
    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
        
    print("Your choice is: " + choice_name)
    print("Now its the computer's turn...")
    
    import random
    comp_choice = random.randint(1,3)
    
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    wait(2)   
    print("Computer's choice is: " + comp_choice_name)
    
    print(choice_name + " V/s " + comp_choice_name)
    wait(1)
    result = (choice - comp_choice + 3) % 3
    
    if result == 0:
        print("Tie")
    elif result == 1:
        print("You Won")
    else:
        print("Computer Won")
    
    print("Do you want to play again? (Y/N)")
    ans = input()
    if ans == 'N' or ans == 'n':
        break
