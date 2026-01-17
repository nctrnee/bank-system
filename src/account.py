from src.validation import (get_validated_input, get_valid_name, get_valid_age, validate_summary)
from src.storage import load_data, dump_data
import random
import json


def generate_acc_number(first_name, middle_name, last_name):
    """Generate account number for new user"""
    block1 = f"{first_name[0]}{middle_name[0]}{last_name[0]}"
    block2 = random.randint(1, 999999)
    return f"{block1}-{block2:06d}"


def generate_temporary_password():
    """Generate temporary password for new user"""
    data = load_data()
    while True:
        password = random.randint(111111, 999999)
        # Check if password is existing in JSON
        if password not in [user['password'] for user in data.values()]:
            return password
        """
        data.values -> get user dict    
        [user['password'] for user in data.values()] -> list of password
        """


def create_new_account():
    """Create account for new user > save to json file"""
    print("\n---SUPPLY NEEDED INFORMATION---")
    last_name = get_validated_input(get_valid_name, "\nLast name: ")
    first_name = get_validated_input(get_valid_name, "\nFirst name: ")
    middle_name = get_validated_input(get_valid_name, "\nMiddle name: ")
    age = get_validated_input(get_valid_age, "\nAge: ")

    last_name, first_name, middle_name, age = validate_summary(last_name, first_name, middle_name, age)
    acc_number = generate_acc_number(first_name, middle_name, last_name)
    temporary_pass = generate_temporary_password()

    # Dict
    account_data = {
        acc_number: {
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": middle_name,
            "age": age,
            "password": temporary_pass
        }
    }

    # Add account to JSON file
    try:
        data = load_data()
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
        
    data.update(account_data)  # Update JSON file
    dump_data(data)  # Save changes

    # Success message
    print("\n---ACCOUNT CREATED!---\nYou may now log with the following credentials:")
    print(f"Username: {acc_number}\nTemporary password: {temporary_pass}")

    
