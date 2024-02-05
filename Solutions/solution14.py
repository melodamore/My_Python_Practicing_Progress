# Write a program to find the greatest of the three numbers entered by the user.

print('This program will find the greatest of 3 numbers. \nPress 1 to continue or any other number to exit: ')
entrance = int(input())
if entrance == 1:
    print('Enter the first number : ')
    num1 = int(input())
    print('Enter the second number : ')
    num2 = int(input())
    print('Enter the third number : ')
    num3 = int(input())

    if num1 > num2 > num3:
        print('---> The greatest number is:', num1)
    else:
        if num2 > num1 > num3:
            print('---> The greatest number is:', num2)
        else:
            if num3 > num2 > num1:
                print('---> The greatest number is:', num3)
            else:
                print('---> All numbers are equal!')
else:
    print('Exited successfully!')
