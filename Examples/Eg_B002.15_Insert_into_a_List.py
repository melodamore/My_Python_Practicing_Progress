# Insert

# Create a list of letters without 'e', 'i', 'n', 'q', 'w' & 'z'
letters = list('abcdfghjklmoprstuvxy')

# Print the letters
print(*letters)
# Print the length of the letters
print('The letters are', str(len(letters)) + '.', 26 - (len(letters)), 'missing!')

# Insert 'e'
letters.insert(4, 'e')
# Print the letters
print('\n', *letters)
# Print the length of the letters
print('The letters are', str(len(letters)) + '.', 26 - (len(letters)), 'missing!')

# Insert 'i'
letters.insert(8, 'i')
# Print the letters
print('\n', *letters)
# Print the length of the letters
print('The letters are', str(len(letters)) + '.', 26 - (len(letters)), 'missing!')

# Insert 'n'
letters.insert(13, 'n')
# Print the letters
print('\n', *letters)
# Print the length of the letters
print('The letters are', str(len(letters)) + '.', 26 - (len(letters)), 'missing!')

# Insert 'q'
letters.insert(16, 'q')
# Print the letters
print('\n', *letters)
# Print the length of the letters
print('The letters are', str(len(letters)) + '.', 26 - (len(letters)), 'missing!')

# Insert 'w'
letters.insert(22, 'w')
# Print the letters
print('\n', *letters)
# Print the length of the letters
print('The letters are', str(len(letters)) + '.', 26 - (len(letters)), 'missing!')

# Insert 'z'
letters.insert(25, 'z')
# Print the letters
print('\n', *letters)
# Print the length of the letters
print('The letters are', str(len(letters)) + '.', 26 - (len(letters)), 'missing!')
