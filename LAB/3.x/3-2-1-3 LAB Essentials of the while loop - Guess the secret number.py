# Set the secret number
secret_number = 777

# Print the welcome message
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Ask the user to enter their guess
number = int(input(":"))

# Keep asking the user to enter their guess until they guess the correct number
while number != secret_number:
    # If the user hasn't guessed the correct number yet, print a message telling them they're stuck in the loop
    print("Ha ha! You're stuck in my loop!")
    # Ask the user to enter their guess again
    number = int(input(":"))
# When the user finally guesses the correct number, exit the loop and print a congratulatory message
else:
    print("Congratulations! You guessed the secret number!")
