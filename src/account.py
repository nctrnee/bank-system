from src.validation import (get_validated_input, get_valid_name, get_valid_age, validate_summary)
from src.storage import load_data, dump_data
import random
import os
import json


def generate_acc_number(firstName, middleName, lastName):
    """Generate account number for new user"""
    block1 = f"{firstName[0]}{middleName[0]}{lastName[0]}"
    block2 = random.randint(1, 999999)
    return f"{block1}-{block2:06d}"


def create_new_account():
    """Create account for new user > save to json file"""
    print("\n---SUPPLY NEEDED INFORMATION---")
    lastName = get_validated_input(get_valid_name, "\nLast name: ")
    firstName = get_validated_input(get_valid_name, "\nFirst name: ")
    middleName = get_validated_input(get_valid_name, "\nMiddle name: ")
    age = get_validated_input(get_valid_age, "\nAge: ")

    lastName, firstName, middleName, age = validate_summary(lastName, firstName, middleName, age)
    acc_number = generate_acc_number(firstName, middleName, lastName)

    # acc_number = generate_acc_number()
    accountData = {
        acc_number: {
            "lastName": lastName,
            "firstName": firstName,
            "middleName": middleName,
            "age": age,
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
    print(f"Username: {acc_number}\nTemporary password: {random.randint(111111, 999999)}")

    
