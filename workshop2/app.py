from banking_pkg import account


def atm_menu(name):
    """
    This function is just a table showing menu bar
    """
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


if __name__ == "__main__":
    print("          === Automated Teller Machine ===          ")
    # task 2: registering name and password
    while True:
        name = input("Enter name to register: ")
        if len(name) > 10:
            print("The maximum length is 10 characters")
            continue
        pin = input("Enter PIN: ")
        if len(pin) > 4:
            print("The maximum length is 4 characters")
            continue
        balance = 0
        print(name, "has been registered with a starting balance of $", balance)
        break
    # task 3: login
    while True:
        print("LOGIN")
        name_to_validate = input("Enter name: ")
        pin_to_validate = input("Enter password: ")
        if name_to_validate == name and pin_to_validate == pin:
            print("Login successful!")
            break
        else:
            print("Invalid credentials")

    while True:
        atm_menu(name)
        option = input("choose an option: ")
        if option == "1":
            account.show_balance(balance)
        elif option == "2":
            balance = account.deposit(balance)
            account.show_balance(balance)
        elif option == "3":
            balance = account.withdraw(balance)
            account.show_balance(balance)
        elif option == "4":
            account.logout(name)
            break
