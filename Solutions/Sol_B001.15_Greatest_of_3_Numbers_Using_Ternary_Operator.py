# Find the greatest of three numbers entered by the user, using a ternary operator

print('This program will find the greatest of three numbers. Press 1 to continue or 0 to exit:')
ent = int(input())

if ent == 1:
    print('Please Enter 3 numbers:')
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    big = num_1 if num_1 > num_2 > num_3 else num_2 if num_2 > num_1 > num_3 else num_3
    print('The greatest number from', num_1, num_2, 'and', num_3, 'is --->', big)
elif ent == 0:
    print('Exited successfully!')
else:
    print('Error!')
