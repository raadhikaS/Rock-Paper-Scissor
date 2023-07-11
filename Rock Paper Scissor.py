import random

options = ("Rock", "Paper", "Scissors")

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

player_choice = input("Enter your choice (Rock, Paper, Scissors): ")
player_choice = player_choice.capitalize()

while player_choice not in options:
    player_choice = input("Invalid input. Please enter a valid choice (Rock, Paper, Scissors): ")
    player_choice = player_choice.capitalize()

computer_choice = random.choice(options)

print(f"Player: {player_choice}")
print(f"Computer: {computer_choice}")
print(determine_winner(player_choice, computer_choice))
