# The if-elif-else ladder

print('This program will make check how much credit you can get from the bank.')
print('Press 1 to continue or 2 to exit:')
entrance = int(input())
name1 = 'Daniel'
code1 = 6085
if entrance == 1:
    print("What is your name?")
    name = input()
    print("Enter your pin:")
    pin = int(input())
    if pin == code1:
        print("How much money do you have in the bank?")
        money = int(input())
        if money < 1000:
            print('Sorry,', name, 'you are eligible for 0 etb credit. Deposit at least 1000 etb to be eligible for our'
                                  'credit services!')
        elif money >= 1000 < 10000:
            print('Dear,', name, 'You are eligible for 10,000.00 etb credit. Please enter the amount:')
            credit = int(input())
            if credit <= 10000:
                print(float(credit), 'etb will be credited to your bank account. Enter 1 to confirm or 0 to'
                                     ' cancel:')
                entrance2 = int(input())
                if entrance2 == 1:
                    print('Request Confirmed! Please check your account within 5 minutes.')
                elif entrance2 == 0:
                    print('Request canceled!')
            elif credit > 10000:
                print('Dear,', name, 'You are eligible for 10,000.00 etb only. Please, try again!')
            else:
                print('Error')
        elif money >= 10000 < 100000:
            print('Dear,', name, 'You are eligible for 100,000.00 etb credit. Please enter the amount:')
            credit2 = int(input())
            if credit2 <= 100000:
                print(float(credit2), 'etb will be credited to your bank account. Enter 1 to confirm or 0 to'
                                      ' cancel:')
                entrance3 = int(input())
                if entrance3 == 1:
                    print('Request Confirmed! Please check your account within 5 minutes.')
                elif entrance3 == 0:
                    print('Request canceled!')
            elif credit2 > 100000:
                print('Dear,', name, 'You are eligible for 100,000.00 etb only. Please, try again!')
            else:
                print('Error')

        elif money >= 100000:
            print('Dear,', name, 'You are eligible for 1,000,000.00 etb credit. Please enter the amount:')
            credit2 = int(input())
            if credit2 <= 1000000:
                print(float(credit2), 'etb will be credited to your bank account. Enter 1 to confirm or 0 to'
                                      ' cancel:')
                entrance3 = int(input())
                if entrance3 == 1:
                    print('Request Confirmed! Please check your account within 5 minutes.')
                elif entrance3 == 0:
                    print('Request canceled!')
            elif credit2 > 1000000:
                print('Dear,', name, 'The bank will give 100,000.00 etb credit only. Please, try again!')
            else:
                print('Error')
    else:
        print('Incorrect Pin. Please try again!')
elif entrance == 2:
    print("Exited successfully!")
else:
    print("Incorrect input. The program exited automatically. Please, try again!")
