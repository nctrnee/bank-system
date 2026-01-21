"""Handle atm operations"""


from src.storage import safely_load, dump_data
from src.acc_creation_utils import is_user_willing


def check_balance(account_number):
    """Show balance from account"""
    data = safely_load()
    balance = data[account_number]["Bank Account Details"]["Balance"]
    print(f"\nBalance: {balance}")


def withdraw(account_number):
    """Subtract amount from balance"""
    data = safely_load()
    while True:
        withdraw_amount = input("\n[X] Cancel\nWithdraw ammount: ").strip()
        if withdraw_amount == "x":
            return
        try:
            withdraw_amount = int(withdraw_amount)
            current_balance = data[account_number]["Bank Account Details"]["Balance"]

            if withdraw_amount > current_balance:
                print("Error: Insufficient balance")
            
            elif withdraw_amount < 500:
                print("Error: Minimun of 500")
            else:
                data[account_number]["Bank Account Details"]["Balance"] -= withdraw_amount
                print(f"\nNew balance: {data[account_number]["Bank Account Details"]["Balance"]}")
                dump_data(data)
                break

        except ValueError:
            print("Error: Invalid character")


def deposit(account_number):
    """Add amount to balance"""
    data = safely_load()

    while True:
        deposit_amount = input('\n[X] Cancel\nDeposit amount: ').strip().lower()
        if deposit_amount == "x":
            return
        try:
            deposit_amount = int(deposit_amount)
            if deposit_amount < 500:
                print("Error: Minimum of 500")
            elif deposit_amount == "x":
                return
            else:
                data[account_number]["Bank Account Details"]["Balance"] += deposit_amount
                print(f"\nNew balance: {data[account_number]["Bank Account Details"]["Balance"]}")
                dump_data(data)
                break
            
        except ValueError:
            print("Error: Invalid character")


def show_atm(account_number):
    """Allow user to do ATM transactions"""
    if is_user_willing("Continue to ATM transactions?"):
        while True:
            user_input = input("""
--------------ATM-----------------                                                   
[1] Check balance
[2] Deposit
[3] Withdraw
[4] Back to user menu                       
> """).strip().lower()
            
            if user_input == "1":
                check_balance(account_number)
            elif user_input == "2":
                deposit(account_number)
            elif user_input == "3":
                withdraw(account_number)
            elif user_input == "4":
                return
            else:
                print("Error: Inavlid input")
