# Ask the user to enter a number and check whether its ASCII value is greater than 80.

char = input('Enter a character (if number, 1-9): ')
print('ASCII value of', char, 'is', ord(char))
print('ASCII value is > 80.') if ord(char) > 80 else print('ASCII value is < 80') if ord(char) < 80 \
    else print('ASCII value = 80')
