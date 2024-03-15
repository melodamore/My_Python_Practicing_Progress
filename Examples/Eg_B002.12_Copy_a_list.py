# Copy

# Create a list of even numbers
even_numbers = [2, 4, 6, 8, 10]

# Print the list
print('Even numbers:', even_numbers)

# Copy the list to another list
even_numbers_2 = even_numbers.copy()

# Print the new list
print('The copies even numbers:', even_numbers_2)

# Make changes to the first list
even_numbers.append(12)

# Print the list
print('Let\'s add 12 to the list:', even_numbers)

# Make changes to the copied list
del even_numbers_2[4]

# Print the list
print('Let\'s delete 10 from the list:', even_numbers_2)
