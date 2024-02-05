# Logical Operators --> 'or' or '|'

(acc1, pass1, name1, f_name1, b_year1, email1) = ('leinad', 6085, 'Daniel', 'Yohannes', 2003,
                                                  'leinad.sennahoy@gmail.com')
(acc2, pass2, name2, f_name2, b_year2, email2) = ('melodamore', 8519, 'Mekdes', 'Yonas', 2004, 'melodamore@gmail.com')

print('This program will help you recover your password when you forget it')
print('Username:')
acc = str(input())
if (acc == acc1) | (acc == acc2):
    print('Password:')
    pass0 = int(input())
    if (pass0 == pass1) | (pass0 == pass2):
        if (acc == acc1) & (pass0 == pass1):
            print('Welcome,', name1, f_name1, 'You have successfully logged in!')
        elif (acc == acc2) & (pass0 == pass2):
            print('Welcome,', name2, f_name2, 'You have successfully logged in!')
    else:
        print('Incorrect password! Press 1 to recover your password or 0 to exit')
        enter = int(input())
        if enter == 1:
            print('What is your first name?')
            name_check = str(input())
            print('What is your last name?')
            f_name_check = str(input())
            print('What is your birth year?')
            b_year_check = int(input())
            if (name_check == name1) | (name_check == name2):
                if (f_name_check == f_name1) | (f_name_check == f_name2):
                    if (b_year_check == b_year1) | (b_year_check == b_year2):
                        if (name_check == name1) & (f_name_check == f_name1) & (b_year_check == b_year1):
                            print('Dear,', acc1, 'Your password is successfully sent to your email address:', email1)
                        elif (name_check == name2) & (f_name_check == f_name2) & (b_year_check == b_year2):
                            print('Dear,', acc2, 'Your password is successfully sent to your email address:', email2)
                    else:
                        print('Unable to confirm your information. Please try again!')
                else:
                    print('Unable to confirm your information. Please try again!')
            else:
                print('Unable to confirm your information. Please try again!')
        elif enter == 0:
            print('Exited successfully!')
        else:
            print('Error!')

else:
    print('Username not found! Please try again!')
