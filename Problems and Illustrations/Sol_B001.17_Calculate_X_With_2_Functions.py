"""
Ask the user to enter a number 'x' and if the number is greater than 2, calculate it with
    'f(x) = x^2 + 5X + 3' else calculate it with 'f(X) = x + 3'
"""

print('This program will calculate a number \'x\' with f(x) = x^2 + 5x + 3 if \'x\' is > 2, else with f(x) = x + 3 .')
pre = (input('Press 1 to continue or 0 to exit:\t'))
if isinstance(pre, int):
    if pre == 1:
        num = (input("Enter a number \'x\':\t"))
        if int(num) > 2:
            solution = (int(num)**2) + (5*int(num)) + 3
            print('f(x) = x^2 + 5x + 3')
            print('f(x) = '+str(num)+'^2 + 5('+str(num)+') +3')
            print('f(x) = '+str(int(num)**2)+' + '+str(num*5)+' + 3')
            print('f(x) =', solution)

        else:
            solution = int(num) + 3
            print('f(x) = x + 3')
            print('f(x) = '+str(num), '+ 3')
            print('f(x) =', solution)

    elif pre == 0:
        print('Exited Successfully!')

    else:
        print('An error has occurred. Please, Enter 1 or 0 and try again!')
else:
    print('An error has occurred. Please, Enter 1 or 0 and try again!')
