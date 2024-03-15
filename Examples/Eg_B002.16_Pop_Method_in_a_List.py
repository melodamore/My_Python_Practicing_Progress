# Pop

# Prompt for a name and create a list of the characters of the name
name = list(input('What is your name?\t'))

# Remove the last character of the name
print('\''+name.pop()+'\'', 'removed. So your name becomes:', * name)

# Remove the first character of the name
print('\nAnd now \''+name.pop(0)+'\'', 'removed. So your name becomes:', * name)
