# Set the secret word
secret_word = "chupacabra"

# Start an infinite loop using the 'while True' statement
while True:
    # Prompt the user to enter a word and store the input in the 'word' variable
    word = input("Enter a secret word: ")
    
    # Check if the 'word' matches the 'secret_word'
    if word == secret_word:
        # If the 'word' matches the 'secret_word', print a success message and terminate the loop
        print(f"You entered: {word}")
        print("You've sucessfully left the loop.")
        break
    else:
        # If the 'word' does not match the 'secret_word', print a failure message and continue the loop
        print(f"You entered: {word}")
        print("Guess again")
