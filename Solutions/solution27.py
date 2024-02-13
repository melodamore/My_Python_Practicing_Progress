"""
The arithmetic progression is obtained by adding the common difference `d` to the first term `a`, successively. The ith
term of the arithmetic progression is given by the following formula: `T(i) = a + (i - 1) * d`.
Ask the user to enter the value of `a`, `d` and `n` (the number of terms), and find all the terms of the AP. Also, find
the sum of all the terms.
"""
a = int(input('Enter the first term \'a\'\t:'))
d = int(input('Enter the common difference \'d\'\t:'))
n = int(input('Enter the number of terms \'n\'\t:'))

i = 1
sum1 = 0

while i <= n:
    term = a + (i - 1) * d
    print('The', str(i)+'th term is', term)
    sum1 = sum1 + term
    i = i + 1

else:
    print('The sum of', n, 'terms is\t:', sum1)
