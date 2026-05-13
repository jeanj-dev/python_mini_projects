# A Number guessing game
# Computer picks a r random number 1 through 100
# User guress until they get it right

import random

secret_number = random.randint(1, 100)
number_of_guesses = 0

# set a flag to control the flow of the game
game_over = False

# keep prompting the user until they guess right
# Track the user's number of guesses
while not game_over:
    
    # Ensure user enter a valid integer
    try:
        user_guess = int(input("Guess a number from 1 to 100: "))
    except ValueError:
        print("Please enter a whole number.")
        continue
        
    if (user_guess < 1 or user_guess > 100):
        print("Out of range. Please enter a number between 1 and 100.")
        continue

    number_of_guesses += 1

    if user_guess == secret_number:
            print(f"you are correct after {number_of_guesses} guesses!")
            game_over = True
    elif user_guess > secret_number:
            print("Guess lower!")
    else:
            print("Guess higher! ")
    
        
