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
        1. Prompt the user with a menu that has two options, 1. Start 2. Instructions 3. Exit
        2. if 1, then contiune
            If 2, then give them the instructions on how to use this program, then bring them back to the start
            if 3, exit the program
        3. Gives them the atomic number of an element
        4. Ask the user to enter the correct element name using the atomic number
        5. Check if the name input is correct,
            if it is, say "Good job!" and add +1 to the score,
            else, give the user the correct answer and ask another question
'''
# Program starts here
import random
from table import periodic_table

# Variables
exit_value = 0
score = 0
question = 0

# Input
# Run while exit_value is 0. If it is anything other than 0, then close the program
while exit_value == 0:
    print("-" * 50)
    print("Welcome to Sagun's Periodic Table Question")
    print("-" * 50)
    print("""1. Start\n2. Instructions\n3. Exit""")
    menu_selection = int(input("Choose your menu selection (1 - 3): "))

# Procress

    # If the menu selection is 1, then start the program
    if menu_selection == 1:
        
        # Let the user choose the range
        print("\n")
        print("Ending range cannot be less than starting range!")
        starting_number = int(input("Enter the periodic starting range (1 - 118): "))
        ending_number = int(input("Enter the periodic ending range (1 - 118): "))
        
        # If starting_number is greater than 118 or less than 1, or ending_number is greater than 118 or less than 1, then end the program
        if (starting_number < 1 or starting_number > 118) or (ending_number < 1 or ending_number > 118):
            print("Invalid range, choose a range between 1 - 118")
            print("\n")
            
        # Else, contiune running the program    
        else:
            
            answer = ' '
            print("\n")
            while answer != 'x':
                # Generate a random number from (1, 118) inclusive.
                atomic_number = random.randint(starting_number, ending_number)
                # peridoic_table refers to the function in table.py
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
                    print("Your answer is correct!")
                    print("You have", score, "out of", question, "right!")
                    
                # Else the user it's wrong with the correct answer
                else:
                    question += 1
                    print("You got it wrong! The correct answer is", element.capitalize())
                    
                    print("\nYou have", score, "out of", question, "right!")
                    print("Keep going you got this!")
                print("\n")
            
    # If the menu selection is 2, then give instructions    
    elif menu_selection == 2:
        print("""
Go to (website) for instructions!

""")

    # If menu selection is 3, exit the program   
    elif menu_selection == 3:
        print("Exiting Program...")
        exit_value = 1

    # Else, print in valid number
    else:
        print("Invalid number!")
    
    
