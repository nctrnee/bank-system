from src.validation import (get_validated_input, get_valid_name, get_valid_age, validate_summary)
from src.storage import load_data, dump_data
import random
import json


def generate_acc_number(first_name, middle_name, last_name):
    """Generate account number for new user"""
    block1 = f"{first_name[0]}{middle_name[0]}{last_name[0]}"
    block2 = random.randint(1, 999999)
    return f"{block1}-{block2:06d}"


def create_new_account():
    """Create account for new user > save to json file"""
    print("\n---SUPPLY NEEDED INFORMATION---")
    last_name = get_validated_input(get_valid_name, "\nLast name: ")
    first_name = get_validated_input(get_valid_name, "\nFirst name: ")
    middle_name = get_validated_input(get_valid_name, "\nMiddle name: ")
    age = get_validated_input(get_valid_age, "\nAge: ")

    last_name, first_name, middle_name, age = validate_summary(last_name, first_name, middle_name, age)
    acc_number = generate_acc_number(first_name, middle_name, last_name)

    # acc_number = generate_acc_number()
    account_data = {
        acc_number: {
            "lastName": last_name,
            "firstName": first_name,
            "middleName": middle_name,
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

    
