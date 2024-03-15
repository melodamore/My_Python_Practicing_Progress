# Formatting Strings

name = input('What is your name?\t')
f_name = input('What is your father\'s name?\t')
age = int(input('How old are you?\t'))
matric = float(input('What is your matric exam result?\t'))
matric_year = input('What year was the exam?\t')
Sentence = 'My name is, %s %s. I am %.0f years old. I got %.2f matric result in the %s examination year!'
values = (name, f_name, age, matric, matric_year)
print(Sentence % values)
