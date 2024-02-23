# Fractions
from fractions import Fraction
from decimal import Decimal

"""
Fraction(x, y)
Return x/y
"""

print("First Part >>>>>>>>>>>>>>>>>>\n")

print(Fraction(128, -26))  # Output: -64/13
print(Fraction(256))  # Output: 256
print(Fraction())  # Output: 0
print(Fraction('2/5'))  # Output: 2/5
print(Fraction(' -5/7'))  # Output: -5/7
print(Fraction('-32.75'))  # Output: -131/4
print(Fraction('5e-3'))  # Output: 1/200
print(Fraction(1.1))  # Output: 2476979795053773/2251799813685248
print(Fraction(2476979795053773, 2251799813685248), "\n")  # Output: 2476979795053773/2251799813685248

print("Second Part >>>>>>>>>>>>>>>>>>\n")
"""
Fraction(Decimal)(x)
Return x/y
"""
print(Fraction(Decimal('1.1')))  # Output: 11/10
print(Fraction(Decimal('2.675438')))  # Output: 1337719/500000
print(Fraction(Decimal(7.85)))  # Output: 4419157134357299/562949953421312
