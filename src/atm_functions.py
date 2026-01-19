"""Handle atm operations"""


from src.storage import safely_load, dump_data


def check_balance(account_number):
    """Show balance from account"""
    data = safely_load()
    balance = data[account_number]["balance"]
    print(f"Balance: {balance}")


def withdraw(account_number):
    """Subtract amount from balance"""
    data = safely_load()
    while True:
        withdraw_amount = input("Withdraw ammount: ").strip()
        try:
            withdraw_amount = int(withdraw_amount)
            current_balance = data[account_number]["balance"]

            if withdraw_amount > current_balance:
                print("Error: Insufficient balance")
            elif withdraw_amount < 500:
                print("Error: Minimun of 500")
            else:
                data[account_number]["balance"] -= withdraw_amount
                print(f"New balance: {data[account_number]["balance"]}")
                dump_data(data)
                break

        except ValueError:
            print("Error: Invalid character")


def deposit(account_number):
    """Add amount to balance"""
    data = safely_load()

    while True:
        deposit_amount = input('Deposit amount: ').strip()
        try:
            deposit_amount = int(deposit_amount)
            if deposit_amount < 500:
                print("Error: Minimun of 500")
            else:
                data[account_number]["balance"] += deposit_amount
                print(f"New balance: {data[account_number]["balance"]}")
                dump_data(data)
                break

        except ValueError:
            print("Error: Invalid character")
