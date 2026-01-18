"""Primary options of user upon running the program"""


from src.acc_creation_utils import (
    get_validated_input,
    get_valid_name,
    get_valid_age,
    validate_summary,
)
from src.login_utils import (
    get_valid_acc_num, 
    is_password_valid, 
    generate_acc_number, 
    generate_temporary_password
)
from src.storage import dump_data, safely_load


def is_user_willing(prompt):
    """Ask to continue before a process"""
    while True:
        proceed = input(f"\n{prompt}\n[Y] Continue [X] Exit\n> ").strip().lower()
        if proceed == "y":
            return True
        elif proceed == "x":
            return False
        else:
            print("Error: Invalid input!")

    
def create_new_account():
    """Create account for new user > save to json file"""
    if is_user_willing("Continue creating account?"):
        print("\n---SUPPLY NEEDED INFORMATION---")
        last_name = get_validated_input(get_valid_name, "\nLast name: ")
        first_name = get_validated_input(get_valid_name, "\nFirst name: ")
        middle_name = get_validated_input(get_valid_name, "\nMiddle name: ")
        age = get_validated_input(get_valid_age, "\nAge: ")

        result = validate_summary(last_name, first_name, middle_name, age)
        if result is None: # Handle abortion in summary section
            return
        
        last_name, first_name, middle_name, age = result
        acc_number = generate_acc_number(first_name, middle_name, last_name)
        temporary_pass = generate_temporary_password()

        # Dict
        account_data = {
            acc_number: {
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "age": age,
                "password": temporary_pass,
            }
        }
        
        # JSON load and dump
        data = safely_load()  # If json does not exist, create
        data.update(account_data)  # Update JSON file
        dump_data(data)  # Save changes

        # Success message
        print("\n---ACCOUNT CREATED!---\nYou may now log with the following credentials:")
        print(f"Username: {acc_number}\nTemporary password: {temporary_pass}")

    else:
        return


def log_in(): 
    """Log in using account number and password"""
    if is_user_willing("Continue logging in?"):
        print("\n---INPUT CREDENTIALS---\n")
        data = safely_load()
        account_number = get_valid_acc_num()
        if is_password_valid(account_number):
            print("---LOG IN SUCCESSFUL---")
            print(f"Hi, {data[account_number]["first_name"]}!")
    else:
        return