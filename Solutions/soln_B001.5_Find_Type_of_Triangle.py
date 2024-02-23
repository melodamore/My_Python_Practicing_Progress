# Ask the user to enter three points and find whether they are collinear. If the points are not collinear then find the
# type of triangle formed by them (equilateral, isosceles or scalene).

print("This program will find whether three points are collinear or not")
print('What are the values of the first coordinate R? \nEnter the x value first then the y value next')
(x1, y1) = (float(input()), float(input()))
print('The first coordinates are', (x1, y1))

print('What are the values of the second coordinate S? \nEnter the x value first then the y value next')
(x2, y2) = (float(input()), float(input()))
print('The second coordinates are', (x2, y2))

print('What are the values of the third coordinate T? \nEnter the x value first then the y value next')
(x3, y3) = (float(input()), float(input()))
print('The third coordinates are', (x3, y3))

"""
Three points are collinear, if the slope of any two pairs of points is the same. 
With three points R, S, and T, three pairs of points can be formed, they are: RS, ST, and RT. 
If the slope of RS = slope of ST = slope of RT, then R, S, and T are collinear points.
"""

r = (x1, y1)
s = (x2, y2)
t = (x3, y3)

print('R =', r)
print('S =', s)
print('T =', t)

# The slope of rs
slope_rs = (y2 - y1) / (x2 - x1)
slope_st = (y3 - y2) / (x3 - x2)
slope_rt = (y3 - y1) / (x3 - x1)

if slope_rs == slope_st == slope_rt:
    print("Slope of RS = Slope of ST = Slope of Rt =", slope_rs)
    print("Since all the three slopes are equal, they are collinear!")
    collinear_test = 1
else:
    collinear_test = 0

# Finding the sides of the points using the distance formula

side_rs = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
side_st = ((x3 - x2)**2 + (y3 - y2)**2)**(1/2)
side_rt = ((x3 - x1)**2 + (y3 - y1)**2)**(1/2)

"""
Equilateral Triangle: An equilateral triangle is a triangle whose three sides all have the same length.
Isosceles Triangle: An isosceles triangle is a triangle that has two sides with the same length.
Scalene Triangle: A scalene triangle is a triangle whose three sides all have different lengths.
"""

if collinear_test == 0:
    if side_rs == side_st == side_rt:
        triangle = 'Equilateral'
    elif (side_rs == side_st) | (side_rs == side_rt) | (side_st == side_rt):
        triangle = 'Isosceles'
    else:
        triangle = 'Scalene'
    print('Side RS:', side_rs)
    print('Side ST:', side_st)
    print('Side RT:', side_rt)
    print('The type of triangle formed by the 3 points is', triangle, 'triangle.')
