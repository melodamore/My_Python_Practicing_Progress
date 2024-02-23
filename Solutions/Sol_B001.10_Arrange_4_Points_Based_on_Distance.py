# Ask the user to enter 4 points and arrange them in order of their distances from the origin.

print('This program will arrange 4 coordinates in order of their distances from the origin')

print('What are the values of the first coordinate? \nEnter the x value first then the y value next')
(x1, y1) = (int(input()), int(input()))
print('The values of the first coordinates are:', (x1, y1))

print('What are the values of the second coordinate? \nEnter the x value first then the y value next')
(x2, y2) = (int(input()), int(input()))
print('The values of the second coordinates are:', (x2, y2))

print('What are the values of the third coordinate? \nEnter the x value first then the y value next')
(x3, y3) = (int(input()), int(input()))
print('The values of the third coordinates are:', (x3, y3))

print('What are the values of the fourth coordinate? \nEnter the x value first then the y value next')
(x4, y4) = (int(input()), int(input()))
print('The values of the fourth coordinates are:', (x4, y4))

d1 = (x1**2 + y1**2)**(1/2)
d2 = (x2**2 + y2**2)**(1/2)
d3 = (x3**2 + y3**2)**(1/2)
d4 = (x4**2 + y4**2)**(1/2)

a = (x1, y1)
b = (x2, y2)
c = (x3, y3)
d = (x4, y4)

print('The distance of the first coordinates', (x1, y1), 'is', d1)
print('The distance of the second coordinates', (x2, y2), 'is', d2)
print('The distance of the third coordinates', (x3, y3), 'is', d3)
print('The distance of the fourth coordinates', (x4, y4), 'is', d4)

print('\n')
print(a)
print(b)
print(c)
print(d)

print('\nThe order of the points based on their distances is as follows:')

if d1 < d2 < d3 < d4:
    value = (a, b, c, d)
elif d1 < d2 < d4 < d3:
    print(a, b, d, c)
elif d1 < d3 < d2 < d4:
    print(a, c, b, d)
elif d1 < d3 < d4 < d2:
    print(a, c, d, b)
elif d1 < d4 < d2 < d3:
    print(a, d, b, c)
elif d1 < d4 < d3 < d2:
    print(a, d, c, b)

elif d2 < d1 < d3 < d4:
    print(b, a, c, d)
elif d2 < d1 < d4 < d3:
    print(b, a, d, c)
elif d2 < d3 < d1 < d4:
    print(b, c, a, d)
elif d2 < d3 < d4 < d1:
    print(b, c, d, a)
elif d2 < d4 < d1 < d3:
    print(b, d, a, c)
elif d2 < d4 < d3 < d1:
    print(b, d, c, a)

elif d3 < d1 < d2 < d4:
    print(c, a, b, d)
elif d3 < d1 < d4 < d2:
    print(c, a, d, b)
elif d3 < d2 < d1 < d4:
    print(c, b, a, d)
elif d3 < d2 < d4 < d1:
    print(c, b, d, a)
elif d3 < d4 < d1 < d2:
    print(c, d, a, b)
elif d3 < d4 < d2 < d1:
    print(c, d, b, a)

elif d4 < d1 < d2 < d3:
    print(d, a, b, c)
elif d4 < d1 < d3 < d2:
    print(d, a, c, b)
elif d4 < d2 < d1 < d3:
    print(d, b, a, c)
elif d4 < d2 < d3 < d1:
    print(d, b, c, a)
elif d4 < d3 < d1 < d2:
    print(d, c, a, b)
elif d4 < d3 < d2 < d1:
    print(d, c, b, a)

elif d1 == d2:
    if d2 < d3 < d4:
        print(a, b, c, d)
    elif d2 < d4 < d3:
        print(a, b, d, c)
    elif d3 < d2 < d4:
        print(c, a, b, d)
    elif d3 < d4 < d2:
        print(c, a, d, b)
    elif d4 < d2 < d3:
        print(d, a, b, c)
    elif d4 < d3 < d2:
        print(d, c, a, b)
    elif d1 == d3:
        if d1 < d4:
            print(a, b, c, d)
        else:
            print(d, a, b, c)
    elif d1 == d4:
        if d1 < d3:
            print(a, b, d, c)
        else:
            print(c, a, b, d)
    elif d1 == d4:
        if d1 < d3:
            print(a, b, c, d)
        else:
            print(c, d, a, b)

elif d1 == d3:
    if d1 < d2 < d4:
        print(a, c, b, d)
    elif d1 < d4 < d3:
        print(a, c, d, b)
    elif d2 < d1 < d4:
        print(b, a, c, d)
    elif d2 < d4 < d1:
        print(b, d, a, c)
    elif d4 < d1 < d2:
        print(d, a, c, b)
    elif d4 < d2 < d1:
        print(d, b, a, c)
    elif d1 == d2:
        if d1 < d4:
            print(a, b, c, d)
        else:
            print(d, a, b, c)
    elif d1 == d4:
        if d1 < d2:
            print(a, c, d, b)
        else:
            print(b, d, a, c)

elif d1 == d4:
    if d1 < d2 < d3:
        print(a, d, b, c)
    elif d1 < d3 < d2:
        print(a, d, c, b)
    elif d2 < d1 < d3:
        print(b, a, d, c)
    elif d2 < d3 < d1:
        print(b, c, a, d)
    elif d3 < d1 < d2:
        print(c, a, d, b)
    elif d3 < d2 < d1:
        print(c, b, a, d)
    elif d2 == d3:
        if d1 < d2:
            print(a, d, b, c)
        else:
            print(b, c, a, d)

elif d2 == d3:
    if d1 < d2 < d4:
        print(a, b, c, d)
    elif d1 < d4 < d2:
        print(a, d, b, c)
    elif d2 < d1 < d4:
        print(b, c, a, d)
    elif d2 < d4 < d1:
        print(b, c, d, a)
    elif d4 < d1 < d2:
        print(d, a, b, c)
    elif d4 < d2 < d1:
        print(d, b, c, a)
    elif d2 == d4:
        if d2 < d1:
            print(b, c, d, a)
        else:
            print(a, b, c, d)


elif d2 == d4:
    if d1 < d2 < d3:
        print(a, b, d, c)
    elif d1 < d3 < d2:
        print(a, c, b, d)
    elif d2 < d1 < d3:
        print(b, d, a, c)
    elif d2 < d3 < d1:
        print(b, d, c, a)
    elif d3 < d2 < d1:
        print(c, b, d, a)
    elif d3 < d1 < d2:
        print(c, a, b, d)

elif d3 == d4:
    if d1 < d2 < d3:
        print(a, b, c, d)
    elif d1 < d3 < d2:
        print(a, c, d, b)
    elif d2 < d1 < d3:
        print(b, a, c, d)
    elif d2 < d3 < d1:
        print(b, c, d, a)
    elif d3 < d2 < d1:
        print(c, d, b, a)
    elif d3 < d1 < d2:
        print(c, d, a, b)


elif d1 == d2 == d3 == d4:
    print(a, b, c, d)

else:
    print('Error! Unable to give order for the points based on their distances from the origin.')
