# Ask the user to enter 4 points and arrange them in order of their distances from the origin.

print('This program will arrange 4 coordinates in order of their x coordinates')

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

a = (x1, y1)
b = (x2, y2)
c = (x3, y3)
d = (x4, y4)

print('\n')
print(a)
print(b)
print(c)
print(d)

print('\nThe order of the points based on their x coordinates is as follows:')

if x1 < x2 < x3 < x4:
    print(a, b, c, d)
elif x1 < x2 < x4 < x3:
    print(a, b, d, c)
elif x1 < x3 < x2 < x4:
    print(a, c, b, d)
elif x1 < x3 < x4 < x2:
    print(a, c, d, b)
elif x1 < x4 < x2 < x3:
    print(a, d, b, c)
elif x1 < x4 < x3 < x2:
    print(a, d, c, b)

elif x2 < x1 < x3 < x4:
    print(b, a, c, d)
elif x2 < x1 < x4 < x3:
    print(b, a, d, c)
elif x2 < x3 < x1 < x4:
    print(b, c, a, d)
elif x2 < x3 < x4 < x1:
    print(b, c, d, a)
elif x2 < x4 < x1 < x3:
    print(b, d, a, c)
elif x2 < x4 < x3 < x1:
    print(b, d, c, a)

elif x3 < x1 < x2 < x4:
    print(c, a, b, d)
elif x3 < x1 < x4 < x2:
    print(c, a, d, b)
elif x3 < x2 < x1 < x4:
    print(c, b, a, d)
elif x3 < x2 < x4 < x1:
    print(c, b, d, a)
elif x3 < x4 < x1 < x2:
    print(c, d, a, b)
elif x3 < x4 < x2 < x1:
    print(c, d, b, a)

elif x4 < x1 < x2 < x3:
    print(d, a, b, c)
elif x4 < x1 < x3 < x2:
    print(d, a, c, b)
elif x4 < x2 < x1 < x3:
    print(d, b, a, c)
elif x4 < x2 < x3 < x1:
    print(d, b, c, a)
elif x4 < x3 < x1 < x2:
    print(d, c, a, b)
elif x4 < x3 < x2 < x1:
    print(d, c, b, a)

elif x1 == x2:
    if x2 < x3 < x4:
        print(a, b, c, d)
    elif x2 < x4 < x3:
        print(a, b, d, c)
    elif x3 < x2 < x4:
        print(c, a, b, d)
    elif x3 < x4 < x2:
        print(c, a, d, b)
    elif x4 < x2 < x3:
        print(d, a, b, c)
    elif x4 < x3 < x2:
        print(d, c, a, b)
    elif x1 == x3:
        if x1 < x4:
            print(a, b, c, d)
        else:
            print(d, a, b, c)
    elif x1 == x4:
        if x1 < x3:
            print(a, b, d, c)
        else:
            print(c, a, b, d)
    elif x1 == x4:
        if x1 < x3:
            print(a, b, c, d)
        else:
            print(c, d, a, b)

elif x1 == x3:
    if x1 < x2 < x4:
        print(a, c, b, d)
    elif x1 < x4 < x3:
        print(a, c, d, b)
    elif x2 < x1 < x4:
        print(b, a, c, d)
    elif x2 < x4 < x1:
        print(b, d, a, c)
    elif x4 < x1 < x2:
        print(d, a, c, b)
    elif x4 < x2 < x1:
        print(d, b, a, c)
    elif x1 == x2:
        if x1 < x4:
            print(a, b, c, d)
        else:
            print(d, a, b, c)
    elif x1 == x4:
        if x1 < x2:
            print(a, c, d, b)
        else:
            print(b, d, a, c)

elif x1 == x4:
    if x1 < x2 < x3:
        print(a, d, b, c)
    elif x1 < x3 < x2:
        print(a, d, c, b)
    elif x2 < x1 < x3:
        print(b, a, d, c)
    elif x2 < x3 < x1:
        print(b, c, a, d)
    elif x3 < x1 < x2:
        print(c, a, d, b)
    elif x3 < x2 < x1:
        print(c, b, a, d)
    elif x2 == x3:
        if x1 < x2:
            print(a, d, b, c)
        else:
            print(b, c, a, d)

elif x2 == x3:
    if x1 < x2 < x4:
        print(a, b, c, d)
    elif x1 < x4 < x2:
        print(a, d, b, c)
    elif x2 < x1 < x4:
        print(b, c, a, d)
    elif x2 < x4 < x1:
        print(b, c, d, a)
    elif x4 < x1 < x2:
        print(d, a, b, c)
    elif x4 < x2 < x1:
        print(d, b, c, a)
    elif x2 == x4:
        if x2 < x1:
            print(b, c, d, a)
        else:
            print(a, b, c, d)


elif x2 == x4:
    if x1 < x2 < x3:
        print(a, b, d, c)
    elif x1 < x3 < x2:
        print(a, c, b, d)
    elif x2 < x1 < x3:
        print(b, d, a, c)
    elif x2 < x3 < x1:
        print(b, d, c, a)
    elif x3 < x2 < x1:
        print(c, b, d, a)
    elif x3 < x1 < x2:
        print(c, a, b, d)

elif x3 == x4:
    if x1 < x2 < x3:
        print(a, b, c, d)
    elif x1 < x3 < x2:
        print(a, c, d, b)
    elif x2 < x1 < x3:
        print(b, a, c, d)
    elif x2 < x3 < x1:
        print(b, c, d, a)
    elif x3 < x2 < x1:
        print(c, d, b, a)
    elif x3 < x1 < x2:
        print(c, d, a, b)


elif x1 == x2 == x3 == x4:
    print(a, b, c, d)

else:
    print('Unable to give order for the points based on their x coordinates')

