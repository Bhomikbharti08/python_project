import time

print("please insert your card")

time.sleep(5)

pin = int(input("enter your atm pin "))

balance = 15000
password = 1234
if pin == 1234:
    while True:
        print('1 = check balance')
        print('2 = withdraw money')
        print('3 = deposit money ')
        print('4 = exit')
        try:
            option = int(input('choose any option'))
        except:
            print('please choose the valid option')
        if option == 1:
            print('----------------------------------')
            print(f'your current balance is {balance}')
        if option ==2:
            withdraw_money = int(input('enter your withdraw amount'))
            if withdraw_money < balance:
                     print('---------------------------------------')
                     balance = balance-withdraw_money
                     print(f'{withdraw_money} is  debited from your account')
                     print(f'your current balance is {balance}')
            else:
                print('you do not have sufficient balance')
        if option == 3:
            deposit_money = int(input('enter your depost amount'))
            balance = balance + deposit_money
            print('---------------------------------------------')
            print(f'{deposit_money} is credited to your account')
            print(f' your current balance is {balance}')
        if option==4:
            print('Thank you for visiting  in our ATM machine .... see you again ')
            break
else:
    print('You entered the wrong pin ... try a gain')












