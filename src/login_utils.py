"""Handle login operations"""

import random
from src.storage import safely_load


def generate_acc_number(first_name, middle_name, last_name):
    """Generate account number for new user"""
    block1 = f"{first_name[0]}{middle_name[0]}{last_name[0]}"
    block2 = random.randint(1, 999999)
    return f"{block1}-{block2:06d}"


def generate_temporary_password():
    """Generate temporary password for new user"""
    data = safely_load
    while True:
        password = random.randint(111111, 999999) 
        password = str(password)
        # Check if password is existing in JSON
        try:
            if password not in [user["password"] for user in data.values()]:
                return password
            #  data.values -> get user dict    
            # [user['password'] for user in data.values()] -> list of password
        except AttributeError:
            return password
    

def get_valid_acc_num():
    """Get validated account number from user that matches JSON/ """
    data = safely_load()
    
    while True:
        account_number = input("Account Number: ").strip()
        if account_number in data:
            return account_number
        elif account_number in ["X", "x"]:
            return
        else:
            print("\nError: Invalid Account Number!")


def is_password_valid(account_number):
    """Get validated password from user that matches JSON/"""
    data = safely_load()

    if account_number is None: 
        return  # Return to main menu
    
    while True:
        password = input("Password: ").strip()
        if data[account_number]["password"] == password:
            return True
        elif password in ["X", "x"]:
            return
        else:
            print("Error: Password incorrect!\n")
