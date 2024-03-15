# Template Strings

# Import 'Template' from 'string'
from string import Template

# Prompt a name
name = input('What is your name?\t')

# Prompt father's name
f_name = input('What is your father\'s name?\t')

# Prompt age
age = input('How old are you?\t')

# Construct a simple sentence using 'Template'
sentence = Template('My name is, $name $f_name. I am $age years old')

# Substitute with keyword arguments
print(sentence.substitute(name=name, f_name=f_name, age=age))
