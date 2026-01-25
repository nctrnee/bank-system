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
    password = f"{random.randint(1, 999999):06d}"
    return password


def get_valid_acc_num() -> str | None:
    """Get validated account number from user that matches JSON/ """
    data = safely_load()
    while True:
        account_number = input("Account Number: ").strip()
        if account_number in data:
            return account_number
        if account_number.lower() == "x":
            return None
        print("\nError: Invalid Account Number!")


def is_password_valid(account_number) -> bool:
    """Get validated password from user that matches JSON/"""
    data = safely_load()

    if account_number is None:
        return False   # Return to main menu

    while True:
        password = input("Password: ").strip()

        if data[account_number]["Bank Account Details"]["Password"] == hash_password(password):
            return True

        if password.lower() == "x":
            return False

        print("Error: Password incorrect!\n")
