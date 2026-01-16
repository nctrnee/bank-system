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
            pass
        elif user_input == "3":
            print("Session ended")
            break
        else:
            print("Error: Invalid input!")


main()
