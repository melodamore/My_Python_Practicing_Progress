# Append

# Create a list of odd numbers from 1 to 9
odd_numbers = [1, 3, 5, 7, 9]

# Print the odd numbers
print(odd_numbers)

# Prompt the next odd number
odd_numbers.append(int(input('What is the next odd number? ')))

# If the user input equals to 11, print 'Correct'
if odd_numbers[5] == 11:
    print('Correct!', *odd_numbers)

# If the user input is different from 11, print 'Wrong!'
else:
    print('Wrong! It is 11.')
