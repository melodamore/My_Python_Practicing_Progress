"""
Ask the user to enter a three-digit number. Call it 'num'. Find the number obtained by reversing the order of the digits
Find the sum of the given number and that obtained by reversing the order of the digits. Finally, find if any digit in
the sum obtained is the same as that in the original number.
"""

print('Enter a 3 digit number : ')
num = input()
if (int(num) < 100) | (int(num) > 999):
    print('Incorrect input')
else:
    (a, b, c) = num
    (a, b, c) = (c, b, a)
    num2 = num[::-1]
    print('The given number is : ', num)
    print('The reversed order of the given number is : ', num2)
    sum1 = int(num)+int(num2)
    if int(sum1) < 1000:
        (d, e, f) = str(sum1)
        print('sum = ', int(sum1))
        if (d == a) | (d == b) | (d == c) | (e == a) | (e == b) | (e == c) | (f == a) | (f == b) | (f == c):
            print('Condition = True (at least one digit in the sum is the same as that in the original)')
        else:
            print('Condition = False (no digit of the sum is same as the original number)')

    else:
        (d, e, f, g) = str(sum1)
        print('sum = ', int(sum1))
        if ((d == a) | (d == b) | (d == c) | (e == a) | (e == b) | (e == c) | (f == a) | (f == b) | (f == c) | (g == a)
           | (g == b) | (g == c)):
            print('Condition = True (at least one digit in the sum is the same as that in the original)')
        else:
            print('Condition = False (no digit of the sum is same as the original number)')
