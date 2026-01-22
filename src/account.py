"""Primary options of user upon running the program"""


from src.acc_creation_utils import (
    get_validated_input,
    get_validated_name,
    get_name,
    get_age,
    get_birthdate,
    get_contact_number,
    get_email,
    select_account_type,
    get_initial_deposit,
    is_user_willing,
    validate_summary
)
from src.login_utils import (
    get_valid_acc_num, 
    is_password_valid, 
    generate_acc_number, 
    generate_temporary_password,
    hash_password
)
from src.user_menu import show_profile
from src.storage import dump_data, safely_load
from src.atm_functions import show_atm


def create_new_account():
    """Create account for new user > save to json file"""
    if is_user_willing("Continue creating account?"):  # Handle mistyped

        # Gather info from user
        print("\n---SUPPLY NEEDED INFORMATION---\n[X] Cancel\n")

        print("PERSONAL INFORMATION")
        last_name = get_validated_name(get_name, "Last name: ")
        if last_name is None:
            return  # Cancel mid session
        first_name = get_validated_name(get_name, "\nFirst name: ")
        if first_name is None:
            return
        middle_name = get_validated_name(get_name, "\nMiddle name: ")
        if middle_name is None:
            return
        birth_date = get_validated_input(get_birthdate)
        if birth_date is None:
            return
        age = get_validated_input(get_age)
        if age is None:
            return

        print("\nCONTACT INFORMATION")
        contact_number = get_validated_input(get_contact_number)
        if contact_number is None:
            return
        email = get_validated_input(get_email)
        if contact_number is None:
            return

        print("\nACCOUNT DETAILS")
        account_type = get_validated_input(select_account_type)
        if account_type is None:
            return
        initial_deposit = get_validated_input(get_initial_deposit)
        if initial_deposit is None:
            return

        # From the gathered info, validate each and return corrected input
        result = validate_summary(
                    last_name,
                    first_name,
                    middle_name,
                    birth_date,
                    age,
                    contact_number,
                    email,
                    account_type,
                    initial_deposit
                    )

        # User aborted
        if result is None:  
            return

        # Unpacking: distributng the values to variables
        (
            last_name,
            first_name,
            middle_name,
            birth_date,
            age,
            contact_number,
            email,
            account_type,
            initial_deposit
        ) = result

        # Generate credentials
        acc_number = generate_acc_number(first_name, middle_name, last_name)
        temporary_pass = generate_temporary_password()  # Hash password

        # Format dict
        account_data = {
            acc_number: {
                "Personal Information": {
                    "Last name": last_name,
                    "First name": first_name,
                    "Middle name": middle_name,
                    "Birthdate": birth_date,
                    "Age": age
                },
                "Contact Details": {
                    "Contact number": contact_number,
                    "Email": email,
                },
                "Bank Account Details": {
                    "Account type": account_type,
                    "Initial deposit": initial_deposit,
                    "Password": hash_password(temporary_pass),
                    "Balance": initial_deposit
                }
            }
        }

        # JSON load and dump
        data = safely_load()  # If json does not exist, create
        data.update(account_data)  # Update JSON file
        dump_data(data)  # Save changes

        # Success message
        print("\n---ACCOUNT CREATED!---\n""You may now log with the following credentials:")
        print(f"Username: {acc_number}\nTemporary password: {temporary_pass}")

    else:
        return


def log_in(): 

    """Log in using account number and password"""
    if is_user_willing("Continue logging in?"):

        print("\n---INPUT CREDENTIALS---")
        print("[X] Back to Main menu\n")
        data = safely_load()
        account_number = get_valid_acc_num()

        if is_password_valid(account_number):
            print("\n---YOU ARE NOW LOGGED IN---")
            print(f"Hi, {data[account_number]["Personal Information"]["First name"]}!")
            # Show user menu
            while True: 
                user_input = input("""
User menu:
[1] Profile
[2] ATM
[3] Log out
> """).strip().lower()
                if user_input == "1":
                    show_profile(account_number)  # Profile
                elif user_input == "2":
                    show_atm(account_number)  # ATM functions
                elif user_input == "3":  # Log out
                    if is_user_willing("Log out?"):
                        return

    else:
        return
