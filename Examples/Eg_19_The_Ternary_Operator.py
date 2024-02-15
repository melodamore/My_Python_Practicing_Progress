# The Ternary Operator

print("Name:")
name = str(input())
print("Age:")
age = int(input())

a = 1 if age >= 18 else 0  # ----> ternary operator

if a == 1:
    print('Welcome,', name, 'Access granted!')
else:
    print('Sorry,', name, 'Access denied!')

