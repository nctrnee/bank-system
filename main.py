from src.account import create_new_account


def main():
    print("---WELCOME TO THE BANK SYSTEM---")
    while True:
        user_input = input(
            """
[1] Create new account
[2] Log in
[3] Exit
> """
        ).strip()

        if user_input == "1":
            create_new_account()
        elif user_input == "2":
            pass # Log in 
        elif user_input == "3":
            print("Session ended")
            break
        else:
            print("Error: Invalid input!")


""" 
Checks if run directly or imported
    if directly: __name__ == __main__
    if imported: __name__ == <module_name>
"""
if __name__ == "__main__":
    main()
