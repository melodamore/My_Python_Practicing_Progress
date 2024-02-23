# Logical Operators --> 'and' or '&'

print('This program will check your identity. Press 1 to continue or 0 to exit')
enter = int(input())
(pin1, name1, age1, nationality1, fin1, phone1, city1) = (6085, 'Daniel Yohannes Kelemewerk', 20, 'Ethiopian', 9453,
                                                          '+251975006387', 'Addis Ababa')
(pin2, name2, age2, nationality2, fin2, phone2, city2) = (8519, 'Mekdes Yonas Abera', 20, 'Ethiopian', 8519,
                                                          '+251967918010', 'Addis Ababa')

if enter == 1:
    print('Enter your Fin:')
    fin = int(input())
    print('Enter your pin:')
    pin = int(input())
    if (pin == pin1) & (fin == fin1):
        print('Name:', name1, '\nAge:', age1, '\nNationality:', nationality1, '\nPhone:', phone1, '\nCity:', city1)
    elif (pin == pin2) & (fin == fin2):
        print('Name:', name2, '\nAge:', age2, '\nNationality:', nationality2, '\nPhone:', phone2, '\nCity:', city2)
    else:
        print('Please check your \'pin\' or your \'fin\'')

elif enter == 0:
    print('Exited Successfully!')
else:
    print('Error!')
