"""User menu options"""

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

[1-8] Edit [Y] Save [X] Cancel
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