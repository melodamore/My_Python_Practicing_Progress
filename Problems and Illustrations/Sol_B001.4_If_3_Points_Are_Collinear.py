# Ask the user to enter three points and find whether they are collinear.

print("This program will find whether three points are collinear or not")
print('What are the values of the first coordinate R? \nEnter the x value first then the y value next')
(x1, y1) = (int(input()), int(input()))
print('The first coordinates are', (x1, y1))

print('What are the values of the second coordinate S? \nEnter the x value first then the y value next')
(x2, y2) = (int(input()), int(input()))
print('The second coordinates are', (x2, y2))

print('What are the values of the third coordinate T? \nEnter the x value first then the y value next')
(x3, y3) = (int(input()), int(input()))
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
else:
    print("Slope of RS =", slope_rs, 'Slope of ST =', slope_st, 'Slope of RT =', slope_rt)
    print("Since all the three slopes are not equal, they are not collinear!")
