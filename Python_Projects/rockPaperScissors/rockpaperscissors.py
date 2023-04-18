# Import the random module
import random

# Initialize the variables
exit = False
user_points = 0
computer_points = 0

# Start the game loop
while exit == False:

    # Define the options for the game
    option = ["rock", "paper", "scissors"]

    # Get the user's input
    user_input = input("Choose, rock, paper, scissors or exit: ")

    # Get the computer's input
    computer_input = random.choice(option)

    # If the user wants to exit the game, print the scores and end the game
    if user_input == "exit":
        print("Game Ended")
        print(f"You won {user_points} and computer won {computer_points}")
        exit = True

    # If the user selects rock
    if user_input == "rock":

        # If the computer also selects rock
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie!")

        # If the computer selects paper
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer wins!")
            computer_points += 1

        # If the computer selects scissors
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("You win!!")
            user_points += 1
   
    # If the user selects paper
    elif user_input == "paper":

        # If the computer selects rock
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You win!")
            user_points += 1

        # If the computer also selects paper
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It is a tie!")

        # If the computer selects scissors
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer win!")
            computer_points += 1

    # If the user selects scissors
    elif user_input == "scissors":

        # If the computer selects rock
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer win!")
            computer_points += 1

        # If the computer selects paper
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You win!")
            user_points += 1

        # If the computer also selects scissors
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It is a tie")

    # If the user's input is not one of the three options, print an error message
    elif user_input not in ["rock", "paper", "scissors"]:
        print("Invalid Input")
