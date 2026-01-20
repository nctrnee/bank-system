"""Handle login operations"""

import random
from src.storage import safely_load, dump_data
from src.acc_creation_utils import (
    get_validated_input,
    get_validated_name,
    get_name,
    get_age,
    get_birthdate,
    get_email,
    get_contact_number,
    select_account_type,
    is_user_willing
)


def generate_acc_number(first_name, middle_name, last_name):
    """Generate account number for new user"""
    block1 = f"{first_name[0]}{middle_name[0]}{last_name[0]}"
    block2 = random.randint(1, 999999)
    return f"{block1}-{block2:06d}"


def generate_temporary_password():
    """Generate temporary password for new user"""
    data = safely_load()
    while True:
        password = random.randint(111111, 999999) 
        password = str(password)
        # Check if password is existing in JSON
        try:
            if password not in [user["Bank Account Details"]["Password"] for user in data.values()]:
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
        if data[account_number]["Bank Account Details"]["Password"] == password:
            return True
        elif password in ["X", "x"]:
            return
        else:
            print("Error: Password incorrect!\n")


def show_profile(account_number):
    """Show profile of user"""
    all_data = safely_load()
    user_data = all_data[account_number]
    personal = user_data["Personal Information"]
    contact = user_data["Contact Details"]
    bank_acc = user_data["Bank Account Details"]
    while True: 
        # Load fresh data each time
       
        user_input = input(f""""
                           
------------------USER PROFILE------------------------
                       
PERSONAL INFORMATION
    Last name: {personal["Last name"]}
    First name: {personal["First name"]}
    Middle name: {personal["Middle name"]}
    Birthdate: {personal["Birthdate"]}
    Age: {personal["Age"]}

CONTACT INFORMATION
    Contact number: {contact["Contact number"]}
    Email: {contact["Email"]}

ACCOUNT DETAILS
    Account number: {account_number}
    Account type: {bank_acc["Account type"]}

[1] Edit 
[2] Back
> """).strip()
        
        if user_input == "1":
            edit_profile(account_number)
            # Reload
            all_data = safely_load()
            user_data = all_data[account_number]
            personal = user_data["Personal Information"]
            contact = user_data["Contact Details"]
            bank_acc = user_data["Bank Account Details"]

        elif user_input == "2":
            return
        else:
            print("Error: Invalid input!")


def edit_profile(account_number):
    """Allow user to edit profile"""
    all_data = safely_load()  # Complete data
    user_data = all_data[account_number]  # Specific user
    personal = user_data["Personal Information"]
    contact = user_data["Contact Details"]
    bank_acc = user_data["Bank Account Details"]

    if is_user_willing("Continue editing profile?"):
        while True: 
            user_input = input(f"""
------------------USER PROFILE------------------------
                           
PERSONAL INFORMATION
[1] Last name: {personal["Last name"]}
[2] First name: {personal["First name"]}
[3] Middle name: {personal["Middle name"]}
[4] Birthdate: {personal["Birthdate"]}
[5] Age: {personal["Age"]}

CONTACT INFORMATION
[6] Contact number: {contact["Contact number"]}
[7] Email: {contact["Email"]}

ACCOUNT DETAILS
[8] Account type: {bank_acc["Account type"]}

[#] Edit [Y] Save [X] Cancel
> """).strip().lower()
        
            if user_input == "x":  # User abort
                if is_user_willing("Cancel editing profile?"):
                    print("Changes discarded")
                    return
            elif user_input == "y":  # Save
                if is_user_willing("Save changes?"):
                    dump_data(all_data)
                    print("Profile updated")
                    return
            # Update
            elif user_input == "1":
                personal["Last name"] = get_validated_name(get_name, "\nLast name: ")
            elif user_input == "2":
                personal["First name"] = get_validated_name(get_name, "\nFirst name: ")
            elif user_input == "3":
                personal["Middle name"] = get_validated_name(get_name, "\nMiddle name: ")
            elif user_input == "4":
                personal["Birthdate"] = get_validated_input(get_birthdate)
            elif user_input == "5":
                personal["Age"] = get_validated_input(get_age)
            elif user_input == "6":
                contact["Contact number"] = get_validated_input(get_contact_number)
            elif user_input == "7":
                contact["Email"] = get_validated_input(get_email)
            elif user_input == "8":
                bank_acc["Account type"] = get_validated_input(select_account_type)
            else:
                print("Error: Invalid input")