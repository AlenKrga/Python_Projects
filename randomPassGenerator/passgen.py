# Ask the user if they want to generate password or not?
# If yes, ask for password lenght
# Generate Password
# Print Password
# If user dont want to generate password, exit program.

import string  # Importing the string module, which contains a collection of string constants
import random  # Importing the random module, which contains functions for generating random numbers

# Creating a list of characters that will be used to generate the password
characters = list(string.ascii_letters + string.digits + "!@#%$&*" + string.ascii_lowercase + string.ascii_lowercase)

# Defining a function to generate a random password
def generate_password():
    password_length = int(input("How long password should be? "))  # Asking the user to input the desired length of the password
    random.shuffle(characters)  # Randomly shuffling the list of characters
    password = []  # Initializing an empty list to store the password characters

    # Generating the password by randomly choosing characters from the shuffled list and appending them to the password list
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)  # Randomly shuffling the password list again

    password = "".join(password)  # Joining the characters in the password list to form a string
    print(password)  # Printing the generated password

# Creating an infinite loop that will repeatedly ask the user if they want to generate a password
while True:
    option = input("Do you want to get a random password? (Yes/No):")  # Asking the user if they want to generate a password
    if option == "Yes" or option == "yes":  # If the user enters "Yes" or "yes", generate a password
        generate_password()
    elif option == "No" or option == "no":  # If the user enters "No" or "no", end the program
        print("Program ended")
        quit()
    else:  # If the user enters anything other than "Yes" or "yes", or "No" or "no", prompt them to enter a valid input
        print("Invalid input, please write Yes or No")
