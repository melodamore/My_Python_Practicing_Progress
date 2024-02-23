"""
Ask the user to enter the coefficients of a1x + b1y + c1 = 0 and a2x + b2y + c2 = 0 and find out
whether the two lines depicted by the above equations are parallel or not.
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
line1 and line2 are parallel, denoted by l1||l2, iff m1 = m2
    --> m1 = m2 => -a1/b1 = -a2/b2 => a1/b1 = a2/b2
line1 and line2 are perpendicular, demoted by l1_|_l2, iff m1m2 = -1 or m2 = -1/m1
    --> m1m2 = -1 => (-a1/b1)(-a2/b2) = -1 => a1a2 + b1b2 = 0
"""

if (int(a1) / int(a2)) == (int(b1) / int(b2)):
    print('The lines are parallel.')
elif (int(a1) * int(a2) + (int(b1) * int(b2))) == 0:
    print('The lines are perpendicular.')
else:
    print('The lines are neither parallel, nor perpendicular.')
