#!/usr/bin/env python3
# Prompt the user for a sentence and print the sentence in a centered box of correct width
# Ask for a sentence
sentence = str(input('Enter a sentence:\t'))

# Assign the length of the sentence to 'length'
length = len(sentence)

# Draw the box
print()
print(' ' * 5, '+', '-' * length, '+')
print(' ' * 5, '|', ' ' * length, '|')
print(' ' * 5, '|', sentence, '|')
print(' ' * 5, '|', ' ' * length, '|')
print(' ' * 5, '+', '-' * length, '+')
print()
input('<Enter> to close the program')
