#------------------------------------------
# Program: To make a peroidic table program that randomly generates a periodic table element
# Author: SD
# Date: 3/3/2023
#------------------------------------------
'''
    Problem: To make a periodic table program
    Input: Periodic Table Answer
    Process: Compute whether the answer is correct or not
    Output: Whether the answer is correct or not
    Psuedocode:
        1. Prompt the user with a menu that has two options, 1. Start 2. Instructions
        2. if 1, then contiune
            If 2, then give them the instructions on how to use this program, then bring them back to the start
            if 3, exit the program
        2. Gives them the atomic number of an element
        2. Ask the user to enter the correct element name using the atomic number
        3. Check if the name input is correct,
            if it is, say "Good job!",
            else, give the user the correct answer and restart the program
        4. Restart the program
'''
# Program starts here
import random
from table import periodic_table

# Variables
exit_value = 0
answer = ' '
score = 0
question = 0

# Input
while exit_value == 0:
    print("-" * 50)
    print("Welcome to Sagun's Periodic Table Question")
    print("-" * 50)
    print("""1. Start\n2. Instructions\n3. Exit""")
    menu_selection = int(input("Choose your menu selection (1 - 3): "))

# Procress
    # If the menu selection is 1, then start the program
    if menu_selection == 1:
        while answer != 'x':
            atomic_number = random.randint(1, 118)
            element = periodic_table(atomic_number)
            print("-" * 50)
            print("What is the element with an atomic number of " + str(atomic_number) + "?")
            answer = input("Type your answer here, (type x for exit): ").lower()
            print("\n")
            
            # Exits the questions if user types in 'x'
            if answer == 'x':
                print("You got", score, "out of", question, "right!")
                print("Exiting...")
            # elif the answer is equal to the element, say you are correct and give them +1 score
            elif answer == element:
                question += 1
                score += 1
                print("Your answer is correct! You have", score, "out of", question, "right!")
            # Else the user it's wrong with the correct answer
            else:
                question += 1
                print("You got it wrong! The correct answer is", element.capitalize())
                print("You have", score, "out of", question, "right!\n\nKeep going you got this!")
            print("\n")
        
        


    # If the menu selection is 2, then give instructions    
    elif menu_selection == 2:
        print("""
- In order to use this program, type the number 1 which will select start.
- The program will give you an atomic number and you have to answer with the correct element.
- In order to answer, you have to type it in!
- If you would like to leave the program afterwards, just type in the letter x. 

""")



    # If menu selection is 3, exit the program   
    elif menu_selection == 3:
        exit_value = 1

    # Else, print in valid number
    else:
        print("Invalid number!")
    
    
