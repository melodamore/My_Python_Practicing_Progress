# Ask the user to enter two numbers a and b and calculate a to the power of b

a = int(input('Enter a number \'a\':\t'))
b = int(input('Enter a number \'b\':\t'))

ans = a
i = 1

while i < b:
    ans = ans * a
    i = i + 1
else:
    print(a, 'the power of', b, 'is', ans)
