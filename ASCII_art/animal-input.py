# Prompt the user to enter text to display in the speech bubble
text = input('What would you like the cat to say? ')

# Determine the length of the input text
text_length = len(text)

# Print the top border of the speech bubble, consisting of underscores
print('            {}'.format('_' * text_length))

# Print the input text inside the speech bubble, surrounded by angle brackets
print('          < {} >'.format(text))

# Print the bottom border of the speech bubble, consisting of hyphens
print('            {}'.format('-' * text_length))

# Print the cat's ears and face
print('          /')
print(' /\_/\   /')
print('( o.o )')
print(' > ^ <')