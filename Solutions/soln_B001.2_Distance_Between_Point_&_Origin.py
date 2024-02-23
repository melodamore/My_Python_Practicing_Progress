# Ask the user to enter the coordinates of a point and find the distance of the point from the origin.

print('This program will calculate the distance between points from the origin(0, 0)')
print('What are the values of the coordinates? \n(Enter the x value first then the y value next)')
(x, y) = (int(input()), int(input()))

print((x, y))

distance = (x**2 + y**2)**(1/2)
# The formula of distance between the origin (0, 0) and a point (x, y) is (x**2 + y**2)**(1/2)

print('The distance between', (x, y), 'and the origin is: ', distance)
