# Rock Paper Scissor using Python
The given code is a simple implementation of the classic game "Rock, Paper, Scissors." It allows a player to enter their choice and then randomly generates a choice for the computer. After that, it determines the winner based on the choices made.

Let's go through the code step by step:

1. First, the code imports the `random` module, which is needed to generate a random choice for the computer.
2. The available options for the game ("Rock," "Paper," and "Scissors") are defined as a tuple named `options`.
3. The function `determine_winner` is defined, which takes two parameters: `player` and `computer`. This function determines the winner based on the choices made. If both choices are the same, it returns "It's a tie!" If the player wins, it returns "You win!" Otherwise, it returns "Computer wins!" The winner is determined by checking the combinations of choices using a series of conditional statements.
4. The player's choice is obtained by prompting the user to enter their choice using the `input` function. The input is then capitalized using the `capitalize` method to ensure consistency in comparison.
5. The code enters a `while` loop to validate the player's choice. It checks if the player's choice is not in the `options` tuple. If it's not a valid choice, the player is prompted again until a valid choice is entered.
6. The computer's choice is generated randomly using the `random.choice` function, which selects a random element from the `options` tuple.
7. The player's choice and the computer's choice are printed to the console using formatted strings.
8. Finally, the `determine_winner` function is called with the player's choice and the computer's choice as arguments, and the result is printed to the console.

Overall, this code provides a basic implementation of the Rock, Paper, Scissors game where a player can play against the computer. It ensures the player's input is valid and determines the winner based on the choices made.
