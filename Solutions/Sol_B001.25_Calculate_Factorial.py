# Ask the user to enter a number and calculate its factorial.

# 1 * 2 * 3 * ... * n

# Ask the user to enter a number
num = int(input('Enter a numbre:\t'))

counter = 1
factorial = 1

while counter <= num:
    factorial = factorial * counter
    counter = counter + 1

print('The factorial of ' + str(num), 'is ' + str(factorial))