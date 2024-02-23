# Ask the user to enter two points (x and y coordinates) and find the distance between them.

print('This program will calculate the distance between two coordinates')
print('What are the values of the first coordinate? \nEnter the x value first then the y value next')
(x1, y1) = (float(input()), float(input()))
print('The first coordinates are', (x1, y1))

print('What are the values of the second coordinate? \nEnter the x value first then the y value next')
(x2, y2) = (float(input()), float(input()))
print('The second coordinates are', (x2, y2))

distance = (((x2 - x1)**2)+((y2 - y1)**2))**(1/2)
# The formula of distance between two points is (((x2 - x1)**2)+((y2 - y1)**2))**(1/2)

print('The distance between', (x1, y1), 'and', (x2, y2), 'is: ', distance)
