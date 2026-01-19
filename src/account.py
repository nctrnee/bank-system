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
    generate_temporary_password
)
from src.storage import dump_data, safely_load


def create_new_account():
    """Create account for new user > save to json file"""
    if is_user_willing("Continue creating account?"):  # Handle mistyped

        # Gather info from user
        print("\n---SUPPLY NEEDED INFORMATION---\n")

        print("PERSONAL INFORMATION")
        last_name = get_validated_name(get_name, "Last name: ")
        first_name = get_validated_name(get_name, "\nFirst name: ")
        middle_name = get_validated_name(get_name, "\nMiddle name: ")
        birth_date = get_validated_input(get_birthdate)
        age = get_validated_input(get_age)

        print("\nCONTACT INFORMATION")
        contact_number = get_validated_input(get_contact_number)
        email = get_validated_input(get_email)

        print("\nACCOUNT DETAILS")
        account_type = get_validated_input(select_account_type)
        initial_deposit = get_validated_input(get_initial_deposit)
        
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
        temporary_pass = generate_temporary_password()

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
                    "Password": temporary_pass,
                    "balance": initial_deposit
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
            print(f"Hi, {data[account_number]["first_name"]}!")
            # Show user menu
            user_input = input("""
[1] Profile
[2] ATM

""").strip()
            if user_input == "1":
                pass
                # Profile section
            elif user_input == "2":
                pass
                # ATM functions

    else:
        return
