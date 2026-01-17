def get_valid_name(prompt):
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


def get_valid_age(prompt):
    """Get valid age"""
    # Constants
    MIN_AGE = 18
    MAX_AGE = 110

    while True:
        try:
            age = input(prompt).strip()
            age = int(age)
            if not (MIN_AGE <= age <= MAX_AGE):
                print("Error: Age not allowed!")
                continue

            return age

        except ValueError:
            print("Error: Numbers only")


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


def get_validated_input(getInput, prompt):
    """Get input and confirm with user"""
    while True:
        value = getInput(prompt)
        print(f"\nYou entered: {value}")
        if is_input_correct():
            return value


def validate_summary(lastName, firstName, middleName, age):
    """Display all inputs from and can be changed"""
    while True:
        user_input = input(
            f"""\n---VERIFY THE INFORMATION BELLOW---\n
[1] Last name: {lastName}
[2] First name {firstName}
[3] Middle name: {middleName}
[4] Age: {age}

[Y] Continue [#] Edit specific detail
> """
        ).strip()

        if user_input in ["y", "Y"]:
            return lastName, firstName, middleName, age
        elif user_input == "1":
            lastName = get_validated_input(get_valid_name, "\nLast name: ")
        elif user_input == "2":
            firstName = get_validated_input(get_valid_name, "\nFirst name: ")
        elif user_input == "3":
            middleName = get_validated_input(get_valid_name, "\nMiddle name: ")
        elif user_input == "4":
            age = get_validated_input(get_valid_age, "\nAge: ")
        else:
            print("Error: Invalid input!")


