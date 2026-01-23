"""Handle login operations"""

import random
import hashlib  # Security purposes
from src.storage import safely_load


def hash_password(password):
    """Hashes password"""
    return hashlib.sha256(password.encode()).hexdigest()
    # hashlib.sha256() = a one-way encryption algorithm
    # .encode() = converts string to bytes (required by hashlib)
    # .hexdigest() = converts encrypted bytes to readable text


def generate_acc_number(first_name, middle_name, last_name):
    """Generate account number for new user"""
    block1 = f"{first_name[0]}{middle_name[0]}{last_name[0]}"
    block2 = random.randint(1, 999999)
    return f"{block1}-{block2:06d}"


def generate_temporary_password():
    """Generate temporary password for new user"""
    data = safely_load()
    while True:
        password = f"{random.randint(1, 999999):06d}"
        # Check if password is existing in JSON
        try:
            if password not in [user["Bank Account Details"]["Password"] for user in data.values()]:
                return password
            # data.values -> get user dict
            # [user['password'] for user in data.values()] -> list of password
        except AttributeError:
            print("attberror")
            # return password


def get_valid_acc_num():
    """Get validated account number from user that matches JSON/ """
    data = safely_load()

    while True:
        account_number = input("Account Number: ").strip()
        if account_number in data:
            return account_number
        elif account_number == "x":
            return
        else:
            print("\nError: Invalid Account Number!")


def is_password_valid(account_number):
    """Get validated password from user that matches JSON/"""
    data = safely_load()

    if account_number is None: 
        return  # Return to main menu
    
    while True:
        password = input("Password: ").strip().lower()
        if data[account_number]["Bank Account Details"]["Password"] == hash_password(password):
            return True
        elif password == "x":
            return
        else:
            print("Error: Password incorrect!\n")
