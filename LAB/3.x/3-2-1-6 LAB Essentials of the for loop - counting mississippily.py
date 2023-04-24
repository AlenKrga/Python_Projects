import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

# Initialize the river variable to 1.
river = 1

# Use a for loop to iterate 5 times.
# The range function generates a sequence of numbers from 0 to 4.
for mississippily in range(5):
    # Inside the loop, print the current value of the river variable and the string "Mississippi".
    # The f-string format the current value of river with the string "Mississippi".
    print(f'{river} Mississippi')
    
    # Pause the program for 1 second before continuing to the next iteration of the loop.
    # This creates a delay between each "Mississippi" output.
    time.sleep(1)
    
    # Increment the river variable by 1 for the next iteration of the loop.
    river += 1

# After the for loop finishes, print the final message "Ready or not, here I come!".
print("Ready or not, Here I come!")
