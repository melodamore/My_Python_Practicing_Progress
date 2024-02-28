"""
Ask the user you for a year, a month (as a number from 1 to 12), and a day (1 to 31), and then prints out the date
with the proper month name.
"""

# List of months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

# Ask the year
year = int(input('Year:\t'))

# If the year is less than 1000, ask for a 4 digits input
while year < 1000:
    year = int(input('Year(4 digits):\t'))

# If the year is greater than 2024, ask for lesser value
while year > 2024:
    year - int(input('Year(<=2024):\t'))

# Ask the Month
month = int(input('Month:\t'))

# If the month is less than 1 or greater than 12, ask again(1-12)
while (month < 1) | (month > 12):
    month = int(input('Month(1-12):\t'))

# Ask the day
day = int(input('Day:\t'))

# If the day is less than 1 or greater than 31, ask again(1-31)
while (day < 1) | (day > 31):
    day = int(input('Day(1-31):\t'))

# Assign an ending for the days
ending = 'th'

# If the days are 1, 21, and 31; set the ending = 'st'
if (day == 1) | (day == 21) | (day == 31):
    ending = 'st'

# If the days are 2, and 22; set the ending = 'nd'
elif (day == 2) | (day == 22):
    ending = 'nd'

# If the days are 3, and 23; set the ending = 'rd'
elif (day == 3) | (day == 23):
    ending = 'rd'

print('\n -->', months[(month - 1)], str(day) + str(ending) + ',', year)
