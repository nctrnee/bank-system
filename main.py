"""Main program"""

from src.account import create_new_account, log_in


def main():
    print("\n---WELCOME TO THE BANK SYSTEM---")
    while True:
        user_input = input(
            """
Main menu:
[1] Create new account
[2] Log in
[3] Exit
> """
        ).strip()

        if user_input == "1":
            create_new_account()
        elif user_input == "2":
            log_in()
        elif user_input == "3":
            print("\nSession ended")
            break
        else:
            print("Error: Invalid input!")


# Checks if run directly or imported
#    if directly: __name__ == __main__
#    if imported: __name__ == <module_name>
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSession ended: Keyboard interrupt")
