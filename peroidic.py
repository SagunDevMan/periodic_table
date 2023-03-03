#------------------------------------------
# Program: To make a peroidic table program that randomly generates a peroidic table
# Author: SD
# Date: 3/3/2023
#------------------------------------------
'''
    Problem: To make a peroidic table program
    Input: Peroidic Table Answer
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
from table import peroidic_table

exit = 0
# Input
while exit == 0:
    print("-" * 50)
    print("Welcome to Sagun's Peroidic Table Question")
    print("-" * 50)
    print("""1. Start\n2. Instructions\n3. Exit""")
    menu_selection = int(input("Choose your menu selection (1 - 3): "))
    print("-" * 50)

# Procress
    if menu_selection == 1:
        atomic_number = random.randint(1, 118)
        element = peroidic_table(atomic_number)
        print("\n")
        print("What is the element with an atomic number of " + str(atomic_number) + "?")
        answer = input("Type your answer here: ").lower()
        print("\n\n")
        if answer == element:
            print("Your answer is correct!")
        else:
            print("You got it wrong! The correct answer is", element.capitalize())
        print("\n")
        
        


        
    elif menu_selection == 2:
        print("You chose 2")



        
    else:
        exit = 1
    
    
