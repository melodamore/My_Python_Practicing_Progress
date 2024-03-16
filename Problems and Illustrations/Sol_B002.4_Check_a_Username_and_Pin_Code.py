#!/usr/bin/env python3
"""
`Write a program that reads in a username and checks the entered PIN code against a database (a list, actually) that
 contains pairs (more lists) of names and PIN codes. If the name/PIN pair is found in the database, print the string
 'Access granted'.
"""

# Store the information of usernames and pins in a list by assigning a variable called 'database'
database = [
    ['daniel', '1234'],  # username: daniel, pin: 1234
    ['efrata', '2345'],  # username: efrata, pin: 2345
    ['ribka', '3456'],  # username: ribka, pin: 3456
    ['yoseph', '4567']  # username: yoseph, pin: 4567
]

# Ask for username
username = input('Username:@')

# Ask for pin
pin = input('PIN code: ')

# set the access and membership status 'unknown'
status = 'unknown'
member = 'unknown'

# If the username and pin are found in 'database', set status to 'Access Granted' and member to 'T'
if [username, pin] in database:
    status = 'Access Granted'
    member = 'T'

# If the username and pin aren't found in 'database', set status to 'Access Denied' and member to 'F'
else:
    status = 'Access Denied'
    member = 'F'

length_status = len(status)
length_user = len(username)

# Print the status in a graphical box style
print('+', '-' * length_status, '+')
print('|', ' ' * length_status, '|')
print('|', status, '|')
print('|', ' ' * length_status, '|')
print('+', '-' * length_status, '+')

# If membership status is 'True', print a welcome message in a box
if member == 'T':
    print('\n')
    print('+', '---------------------------------------' + '-' * length_user + '------ +')
    print('|    Welcome!', 'You are logged in as -->[' + ' @' + username + ' ]', '    |')
    print('+ --------------------------------------' + '-' * length_user + '--------+')
    print('\n')

# Prompt a final exit button
input('<Enter> to exit')
