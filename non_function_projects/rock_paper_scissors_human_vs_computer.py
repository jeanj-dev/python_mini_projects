# This program simulates a game of Rock, Paper, Scissors
# computer vs human

import random 

# Available choices in the game
choices = ('rock', 'paper', 'scissors')

# Initialize player scores
computer_score = 0
human_score = 0

# Announce the game
print("A 10 round-game of rock, paper, scissors! Human vs Machine!\n")

# Play 10 rounds
for round_num in range(10):
    
    # Keep asking until the human gives a valid choice
    while True:
        human_player = input("Type your choice (rock, paper, scissors): " ).strip().lower()

        if human_player in choices:
            break

        print("Invalid choice! Try again!")

    computer = random.choice(choices)

    # Show their choices
    print(f"You chose: {human_player} | Computer chose: {computer}")

    # check for tie
    if human_player == computer:
        print(f"Round {round_num + 1}: Tie!\n")
    
    # Check if human player wins the round
    elif (
        (human_player == 'rock' and computer == 'scissors') or
        (human_player == 'paper' and computer == 'rock') or
        (human_player == 'scissors' and computer == 'paper')
    ):
        human_score += 1
        print(f"Round {round_num + 1} 🎆 you win this round\n")
    
    # Otherwise, computer wins the round
    else:
        computer_score += 1
        print(f"Round {round_num + 1} 🎆 computer wins this round\n")

# Display final score
print(f"Total score for you: {human_score} points")
print(f"Total score for computer: {computer_score} points")

# Determine the overall winner
if human_score > computer_score:
    print("🏆 you win the game")
elif human_score < computer_score:
    print("🏆 computer wins the game")
else:
    print("🤝 The game is a tie!")

