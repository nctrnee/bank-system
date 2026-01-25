"""User menu options"""

from src.storage import safely_load, dump_data
from src.login_utils import hash_password
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

        user_input = input(f"""

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


def change_password(account_number):
    """Allow user to change password"""
    MIN_MAX = 6
    MAX_ATTEMPT = 3

    if not is_user_willing("Change password?"):
        return

    while True:
        data = safely_load()
        new_pasword = input("\nEnter new password: ").strip()

        if not new_pasword.isnumeric():
            print("Password must contain only numbers")
            continue
        if len(new_pasword) != MIN_MAX:
            print(f"Password must be exactly {MIN_MAX} digits")
            continue

        counter = 0
        while True:
            verified_new_pasword = input("\nEnter again new password: ").strip()
            if verified_new_pasword == new_pasword:
                data[account_number]["Bank Account Details"]["Password"] = hash_password(new_pasword)
                dump_data(data)
                print("Password change successful!")
                return

            counter += 1
            if counter == MAX_ATTEMPT:
                print("Limit reached.")
                return
            print(f"Password mismatched! Attempts remaining: {MAX_ATTEMPT - counter}")


def edit_profile(account_number):
    """Allow user to edit profile"""
    all_data = safely_load()
    user_data = all_data[account_number]
    personal = user_data["Personal Information"]
    contact = user_data["Contact Details"]
    bank_acc = user_data["Bank Account Details"]

    if not is_user_willing("Continue editing profile?"):
        return

    # Dictionary mapping: input -> (data_dict, key, validation_function, prompt)
    field_map = {
        "1": (personal, "Last name", get_name, "\nLast name: "),
        "2": (personal, "First name", get_name, "\nFirst name: "),
        "3": (personal, "Middle name", get_name, "\nMiddle name: "),
        "4": (personal, "Birthdate", get_birthdate, None),
        "5": (personal, "Age", get_age, None),
        "6": (contact, "Contact number", get_contact_number, None),
        "7": (contact, "Email", get_email, None),
        "8": (bank_acc, "Account type", select_account_type, None),
    }

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

        # Cancel
        if user_input == "x":
            if is_user_willing("Cancel editing profile?"):
                print("Changes discarded")
                return
            continue

        # Save
        if user_input == "y":
            if is_user_willing("Save changes?"):
                dump_data(all_data)
                print("Profile updated")
                return
            continue

        # Handle field updates
        if user_input in field_map:
            # Unpack: copy info of right var into left var
            data_dict, key, validator, prompt = field_map[user_input]

            # Get new value
            if prompt:  # If there is a prompt (name fields)
                new_value = get_validated_name(validator, prompt)
            else:  # For other fields
                new_value = get_validated_input(validator)

            # Only update if user didn't cancel (new_value is not None)
            if new_value is not None:
                data_dict[key] = new_value  # Replace the old value
            # If None, just continue the loop without updating
        else:
            print("Error: Invalid input")
