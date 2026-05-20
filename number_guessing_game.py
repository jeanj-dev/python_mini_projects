# A Number guessing game
# Computer picks a random number from 1 through 100
# User guesses until they reach the maximum guesses

import random

secret_number = random.randint(1, 100)
number_of_guesses = 0
maximum_guesses = 10

# set a flag to control the flow of the game
game_over = False

# Inform user how many guesses they have left
print(f"Guess a number from 1 to 100. You have {maximum_guesses} guesses. ")

# keep prompting the user until they guess right
while not game_over:
    
    # Ensure user enter a valid integer
    try:

        user_guess = int(input("Guess a number from 1 to 100. "))
    except ValueError:
        print("Wrong input! Please enter a whole number.")
        continue
        
    if (user_guess < 1 or user_guess > 100):
        print("Out of range. Please enter a number between 1 and 100.")
        continue

    # Track the user's number of guesses
    number_of_guesses += 1    

    if user_guess == secret_number:
        print(f"You are correct after {number_of_guesses} guess{'es' if number_of_guesses != 1 else ''}.")
        game_over = True

    elif number_of_guesses == maximum_guesses:
        print("You reached the maximum number of guesses.")
        print(f"The correct number was {secret_number}.")
        game_over = True

    elif user_guess > secret_number:
        guesses_left = maximum_guesses - number_of_guesses
        print("Guess lower!")
        print(f"You have {guesses_left} guess{'es' if guesses_left != 1 else ''} left.")

    else:
        guesses_left = maximum_guesses - number_of_guesses
        print("Guess higher!")
        print(f"You have {guesses_left} guess{'es' if guesses_left != 1 else ''} left.")
    
    
        
