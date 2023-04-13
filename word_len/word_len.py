# Get a word from the user
word = input("Enter a word: ")

# Get the index of the character to print from the user
num_selected = int(input("Enter position of char to print: "))

# Use a loop to repeatedly ask for input until a valid index is entered
while True:
    # Check if the index is within the range of the word
    if num_selected < len(word):
        # If the index is valid, print the character at that position in the word
        print("The letter at position " + str(num_selected) + " is " + word[num_selected])
        break  # Exit the loop
    else:
        # If the index is out of range, print an error message and ask for a new input
        print("Index is out of range")
        num_selected = int(input("Enter position of char to print: "))
