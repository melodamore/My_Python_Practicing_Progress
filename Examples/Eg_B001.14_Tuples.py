# Tuples

tup1 = (1, 2, 3)

print(tup1)  # Output: (1, 2, 3)

(a, b, c) = tup1

print("The first element of tup1 is: ", a)  # Output: The first element of tup1 is:  1
print('The second element of tup2 is: ', b)  # Output: The second element of tup2 is:  2
print('The third element of tup3 is: ', c)  # Output: The third element of tup3 is:  3

tup2 = (6085, 'Daniel')
tup3 = (1221, 'Efrata')

print(tup2)  # Output: (6085, 'Daniel')
print(tup3)  # Output: (1221, 'Efrata')

(code1, name1) = tup2
(code2, name2) = tup3

print('The code of ', name1, 'is ', code1, '\nThe code of ', name2, 'is ', code2)
# Output: The code of  Daniel is  6085
#         The code of  Efrata is  1221

print('What year is it in Ethiopia?')  # Output: What year is it in Ethiopia?
year_ec = int(input())
print('What year is it in America?')  # Output: What year is it in America?
year_gc = int(input())
print('It is ', year_ec, 'in Ethiopia and ', year_gc, 'in America.')
# Output: It is xxxx in Ethiopia and yyyy in America.
(year_ec, year_gc) = (year_gc, year_ec)
print('But now it is ', year_ec, 'in Ethiopia and ', year_gc, 'in America.')
# Output: But now it is yyyy in Ethiopia and xxxx in America.
