# Ask the user to enter a number and calculate its factorial.

# 1 * 2 * 3 * ... * n

num = int(input('Enter a number:\t'))
factorial = 1  # initializer
i = 1  # counter

while i <= num:
    factorial = factorial * i
    i = i + 1

print('The factorial of', num, 'is', factorial)
