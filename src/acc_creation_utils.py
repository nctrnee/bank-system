"""Handle accoun creation"""


def get_name(prompt):
    """Get valid name"""
    allowed_chars = "abcdefghijklmnopqrstuvwxyz -'"

    while True:
        name = input(prompt).strip().title()

        # Checks if empty
        if not name:
            print("Error: Empty field!")
            continue

        # Checks allowed chars
        if not all(char.lower() in allowed_chars for char in name):
            print("Error: Invalid character!")
            continue

        # Checks min/max length
        if not (2 <= len(name) <= 20):
            print("Error: Must be between 2-20 characters")
            continue

        return name
    

def get_birthdate():
    """Get and format birthdate as MM/DD/YYYY"""
    while True:
        birthdate = input("\nBirthdate (MM/DD/YYYY): ")
        
        # Remove separators
        clean = birthdate.replace("/", "").replace("-", "").replace(" ", "")
        
        # Check if 8 digits
        if len(clean) == 8 and clean.isdigit():
            # Split into parts
            month, day, year = clean[:2], clean[2:4], clean[4:]
            
            # Validation
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and 1900 <= int(year) <= 2025:
                return f"{month}/{day}/{year}"
            else:
                print("Error: Invalid date")
        else:
            print("Error: Enter 8 digits (MMDDYYYY)")


def get_age():
    """Get valid age"""
    # Constants
    MIN_AGE = 18
    MAX_AGE = 110

    while True:
        try:
            age = input("\nAge: ").strip()
            age = int(age)
            if not (MIN_AGE <= age <= MAX_AGE):
                print("Error: Age not allowed!")
                continue

            return age

        except ValueError:
            print("Error: Numbers only")


def get_contact_number():
    """Get 11-digit contact number"""
    while True:
        contact = input("Contact number (09XX-XXX-XXXX):  ").strip()
        # Remove dash and space
        clean = contact.replace("-", "").replace(" ", "")
        
        # Validate
        if clean.startswith("09") and len(clean) == 11 and clean.isdigit():
            # Format
            formatted = f"{clean[:4]}-{clean[4:7]}-{clean[7:]}"
            # :4 -> (from start to index 4, not including 4)
            return formatted
        
        else:
            print("Error: Invalid format. Example: 0912-345-6789")


def get_email():
    """Get email - optional, can skip by pressing Enter"""
    while True:
        email = input("\nEmail (or press Enter to skip): ").strip()
        
        # Allow skipping
        if email == "":
            return None
        
        # Validation
        if "@" in email and "." in email.split("@")[-1]:
            return email.lower()
        else:
            print("Error: Invalid email format (user@example.com)")


def select_account_type():
    """Select account type: Checking/Saving"""
    while True:
        account_type = input("""Account Type:
[1] Checkings
[2] Savings
> """).strip()
        
        if account_type == "1":
            return "Checkings"
        elif account_type == "2":
            return "Savings"
        else:
            print("Error: Invalid input")


def get_initial_deposit():
    """Get initial deposit from new user"""
    while True:
        initial_deposit = input("\nInitial deposit (500 Minimum): ")
        try:
            initial_deposit = int(initial_deposit)
            if initial_deposit < 500:
                print("Error: 500 Minimun")
            else:
                return initial_deposit
        except ValueError:
            print("Error: Invalid character!")


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


def is_input_correct():
    """Confirmation for every input"""
    while True:
        user_input = input("Proceed? [Y] Yes [N] No\n> ").strip().lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Error: Invalid input!")


def get_validated_name(get_input, prompt):
    """Get name and confirm with user"""
    while True:
        value = get_input(prompt)
        print(f"\nYou entered: {value}")
        if is_input_correct():
            return value


def get_validated_input(get_input):
    """Get input and confirm with user"""
    while True:
        value = get_input()
        print(f"\nYou entered: {value}")
        if is_input_correct():
            return value


def validate_summary(last_name, first_name, middle_name, birth_date, age,
                     contact_number, email, account_type, initial_deposit):
    """Display all inputs from user to finalize"""
    while True:
        user_input = input(f"""
\n---VERIFY THE INFORMATION BELLOW---
                           
PERSONAL INFORMATION
[1] Last name: {last_name}
[2] First name: {first_name}
[3] Middle name: {middle_name}
[4] Birthdate: {birth_date}
[5] Age: {age}

CONTACT INFORMATION
[6] Contact number: {contact_number}
[7] Email: {email}

ACCOUNT DETAILS
[8] Account type: {account_type}
[9] Initial deposit: {initial_deposit}

[Y] Continue [#] Edit specific detail [X] Cancel
> """).strip()
        
        # If user is satisifed with the info
        if user_input in ["y", "Y"]:  
            return (last_name, first_name, middle_name, birth_date, age,
                    contact_number, email, account_type, initial_deposit)
        
        # To update
        elif user_input == "1":
            last_name = get_validated_name(get_name, "\nLast name: ")
        elif user_input == "2":
            first_name = get_validated_name(get_name, "\nFirst name: ")
        elif user_input == "3":
            middle_name = get_validated_name(get_name, "\nMiddle name: ")
        elif user_input == "4":
            birth_date = get_validated_input(get_birthdate)
        elif user_input == "5":
            age = get_validated_input(get_age)
        elif user_input == "6":
            contact_number = get_validated_input(get_contact_number)
        elif user_input == "7":
            email = get_validated_input(get_email)
        elif user_input == "8":
            account_type = get_validated_input(select_account_type)
        elif user_input == "9":
            initial_deposit = get_validated_input(get_initial_deposit)
       
        # User aborted
        elif user_input in ["x", "X"]:  
            print("\nAccount creation cancelled!")
            return
        
        else:
            print("Error: Invalid input!")


