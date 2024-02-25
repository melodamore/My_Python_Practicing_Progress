"""
Operators Supported in Numbers
"""
print('Operations:')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Power')
print('6. Modulo')
choice = int(input('Choose Operation:\t'))

if choice == 1:
    print('Addition')
    a = int(input('Enter the first number:\t'))
    b = int(input('Enter the second number:\t'))
    sumab = a + b
    print('\nThe result of ', a, '+', b, 'is:', sumab)
elif choice == 2:
    print('Subtraction')
    a = int(input('Enter the first number:\t'))
    b = int(input('Enter the second number:\t'))
    subab = a - b
    print('\nThe result of ', a, '-', b, 'is:', subab)
elif choice == 3:
    print('Multiplication')
    a = int(input('Enter the first number:\t'))
    b = int(input('Enter the second number:\t'))
    mulab = a * b
    print('\nThe result of', a, '*', b, 'is:', mulab)
elif choice == 4:
    print('Division')
    a = int(input('Enter the first number:\t'))
    b = int(input('Enter the second number:\t'))
    divab = a / b
    print('\nThe result of', a, '/', b, 'is:', divab)
elif choice == 5:
    print('Power')
    a = int(input('Enter the first number:\t'))
    b = int(input('Enter the second number:\t'))
    powerab = a ** b
    print('\nThe result of', a, "^", b, 'is:', powerab)
elif choice == 6:
    a = int(input('Enter the first number:\t'))
    b = int(input('Enter the second number:\t'))
    modab = a % b
    print('\nThe result of', a, '%', b, 'is:', modab)
else:
    print('Please enter a number between 1 and 6.')
