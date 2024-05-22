from deposit import deposits
import balance
from withdraw import withdrawl
import bill

init_balance = 0
acc_balance = 0
new_withdrawal = 0
real_balance = 0
new_deposit = 0
users = {'IMONIDE PRECIOUS': '1234', 'JANE JAMES': '5566', 'ABBY WHITE': '4980'}
a = 0
while a != 3:
    try:
        pin = input("please input your pin: ")

        for x, y in users.items():
            if y == pin:
                print(f'welcome to our app {x}')
                break
            else:
                print("Wrong Password")
        break
    except:
        print("invalid input try again")


    again = input("do you want to try again? ")
    aga_in = again.lower()

    if aga_in == "y" or "yes" :

        if a == 0:
            print("you have 2 trial left")

        elif a == 1:
            print("you have 1 trial left")

        elif a == 2:
            print("you have been blocked")
            break

    a += 1





i = "y" or "yes"
while i == "y" or "yes":
    print("choose your operation \n"
          "1 for balance \n"
          "2 for Withdrawal \n"
          "3 for Deposit \n"
          "4 for pay utility \n")


    choice = int(input())

# call withdrawal function
    if choice == 2:
        if init_balance < 1:
            print("your balance is too low to withdraw, pls deposit first")

        else:
            new_withdrawal = int(input("how much do you want to withdraw: "))
            init_balance = withdrawl(init_balance, new_withdrawal)

# call deposit function
    if choice == 3:

        new_deposit = int(input("how much do you want to deposit: "))

        init_balance = deposits(init_balance, new_deposit, new_withdrawal)
        #init_balance = deposits(init_balance, new_deposit, new_withdrawal)
        # print("this is real balance:", real_balance)

# call balance function
    if choice == 1:
        if init_balance < 1:
            print("your balance is too low please deposit")
            balance.balances(init_balance)
        else:
            balance.balances(init_balance)
            #real_balance = balance.balances(init_balance, new_deposit, new_withdrawal)

# call function to pay bill
    if choice == 4:
        if init_balance < 1:
            print("Your balance is too low to pay bills please deposit")
        else:
            bill.paybill()
            bill_choice = int(input())
            bill.electric_bill(bill_choice)
            elect_choice = int(input())
            bill.benin_bill(elect_choice)
            pay = int(input())
            cust_num = float(input("customer number "))
            pin = int(input("input pint to pay "))
            bill.pin_verification(pin)
            bill.bill_pay(init_balance, pay)

    if choice > 4:
        print("invalid option")


    a = str(input("do you want to perform another transaction?: Y or N: "))
    i = a.lower()
