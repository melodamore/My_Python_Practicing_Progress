# Ask the user to enter two points and find if they are at equal distances from the origin.

print('This program will calculate the distances of two points from the origin and tells if they are at equal distances'
      'from the origin or not')

print('What are the values of the first coordinate? \nEnter the x value first then the y value next')
(x1, y1) = (int(input()), int(input()))
print('The values of the first coordinates are:', (x1, y1))

print('What are the values of the  coordinate? \nEnter the x value first then the y value next')
(x2, y2) = (int(input()), int(input()))
print('The values of the first coordinates are:', (x2, y2))

distance1 = (x1**2 + y1**2)**(1/2)
distance2 = (x2**2 + y2**2)**(1/2)

print('The distance between the first coordinates', (x1, y1), 'and the origin is:', distance1)
print('The distance between the second coordinates', (x2, y2), 'and the origin is:', distance2)

if distance1 == distance2:
    print('Conclusion: They are at equal distances from the origin')
else:
    print('Conclusion: They are not at equal distances from the origin')
