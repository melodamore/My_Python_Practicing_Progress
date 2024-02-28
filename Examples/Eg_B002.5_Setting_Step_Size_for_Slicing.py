# Setting Step Size for Slicing

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(integers)

# By adding the step size at the end of slicing
print(integers[0:12])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(integers[0:12:1])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(integers[0:12:2])  # Output: [1, 3, 5, 7, 9, 11]
print(integers[1:12:2])  # Output: [2, 4, 6, 8, 10, 12]
print(integers[2:10:3], '\n')  # Output: [3, 6, 9]

# By using a shortcut
print(integers[::2])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(integers[::4], '\n')  # Output: [1, 5, 9]

# Negative step size
print(integers[8:3:-1])  # Output: [9, 8, 7, 6, 5]
print(integers[10:0:-2])  # Output: [11, 9, 7, 5, 3]
print(integers[::-3])  # Output: [12, 9, 6, 3]
print(integers[5::-2])  # Output: [6, 4, 2]
print(integers[:5:-2])  # Output: [12, 10, 8]
