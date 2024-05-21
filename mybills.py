def bills():
    print("choose your option \n"
          "1 for nepa bill \n"
          "2 for dstv")
    return

def nepa_bill(pick_option):
    if pick_option == 1:
        print("input bill amount ")

def calc_bill(init_balance, bill_amount):
    init_balance -= bill_amount
    print("purchase successful")
    print("your current balance is",init_balance)


