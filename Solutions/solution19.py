"""
Ask the user to enter the values of a1, a2, b1, b2, c1, and c2 and find whether the lines are
parallel, or if they overlap or intersect.
"""

print('Enter the coefficients of a1x + b1y + c1 = 0')
a1 = input('a1:\t')
b1 = input('b1:\t')
c1 = input('c1:\t')

print('Now enter the coefficients of a2x + b2y + c2 = 0')
a2 = input('a2:\t')
b2 = input('b2:\t')
c2 = input('c2:\t')

print('The lines are', a1+'x +', b1+'y +', c1, '= 0 and', a2+'x +', b2+'y +', c2, '= 0')

"""
line1 and line2 are parallel, iff m1 = m2
    --> m1 = m2 => -a1/b1 = -a2/b2 => a1/b1 = a2/b2
line1 and line2 overlap if a1/a2 = b1/b2 = c1/c2
line1 and line2 intersect if a1/a2 != b1/b2
"""

if (int(a1) / int(a2)) == (int(b1) / int(b2)):
    if (int(a1) / int(a2)) == (int(b1) / int(b2)) == (int(c1) / int(c2)):
        print('The lines overlap')
    else:
        print('The lines are parallel')
else:
    print('The lies intersect')
