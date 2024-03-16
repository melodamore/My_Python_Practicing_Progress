"""
Ask the user to enter a four-digit number and check whether the sum of the first and the last digits is same as the sum
of the second and the third digits. if the answer is true then obtain a number in which the second and the third digit
are one more than that in the given number. Example: Number 5342, sum of the first and the last digit = 7 that of the
second and the third digit = 7. New number: 5452
"""

ent = (input('Enter a four digit number:\t'))
if (int(ent) >= 1000) and (int(ent) <= 9999):
    (a, b, c, d) = ent
    sum_of_1_4 = int(a) + int(d)
    sum_of_2_3 = int(b) + int(c)

    print('The number you entered is', str(ent) + '. and The sum of the first and the last digits', a, '+', d, '=',
          sum_of_1_4, '\nWhile the sum of the second and the third digits', b, '+', c, '=', sum_of_2_3)
    if sum_of_1_4 == sum_of_2_3:
        print('So, the sum of the first and the last digits is same as the sum of the second and the third digits.')
        print('The new number is:', str(a)+(str(int(b)+1))+(str(int(c)+1))+str(d))
    else:
        print('So, the sum of the first and the last digits is not same as the sum of the second and the third digits.')

else:
    print('Please enter a 4 digits number and try again.')
