# this module consists task 4

def show_balance(balance):
    """
    input: balance
    return: nothing
    this is just printing balance
    """
    print("the balance is $", balance)


def deposit(balance) -> float:
    """
    input: amount the user wants to add
    return: new_bal: updated balance
    """
    amount = input("Enter amount to deposit: ")
    new_bal = balance+float(amount)
    return new_bal


def withdraw(balance) -> float:
    """
    input: amount the user wants to withdraw
    return: new_bal: updated balance after withdrawing
    """
    amount = input("Enter amount to withdraw: ")
    new_bal = balance-float(amount)
    if new_bal < 0:
        print("where are you going to get that money?")
        return balance
    return new_bal


def logout(name):
    """
    Exiting the app after showing a message
    """
    print("Goodbye", name, "!")
