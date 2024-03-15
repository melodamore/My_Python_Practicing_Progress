# Assigning to Slices

print('Program 1:')

# Create a list of name characters
name = list('Daniel')

# print the current name
print('\nMy name is', *name)

# Prompt a name change
name[3:] = list(input('Enter a name that starts with \'Dan\': Dan'))
print('And now my name becomes,', *name, '\n')

print('Program 2:\n')

# Create a list of name starting and ending characters
name = list('Dl')

# Prompt a name that starts with 'D' and ends with 'l'
name[1:1] = list(input('Complete the name D____L:'))

# If the user inputs 'aniel' and the name becomes 'Daniel', print 'Correct'
if name == list('Daniel'):
    print('Correct, ', *name)

# If the name doesn't become 'Daniel', print 'Wrong!'
else:
    print('Wrong! It is \'Daniel\'')
