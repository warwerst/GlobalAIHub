"""
Code The Hangman Game
You are free on this assignment.
You can set the rules yourself.There is only one thing expected of you
When enter the game, the user's name should be pressed to the screen.
For example: "Welcome John"
When the game is over, exit game.
So let the game end.

"""

x = input("Please enter naem")
print(f"Welcome {x}")

word = "secret"
guesses: str = ""
while True:
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("")
    guess = input("Guess a character:")
    guesses += guess

    if guess not in word:
        print("Wrong!")


