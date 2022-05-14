def show_homepage():
    """
    This function is just a table showing menu bar
    """
    print("")
    print("          === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations       |")
    print("------------------------------------------")
    print("|                5.  Exit      |")
    print("------------------------------------------")


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation_string = "{} donated ${}".format(username, donation_amt)
    print("thank you for your donation!")
    return donation_string


def show_donations(donations):
    print("\n--- All Donations---")
    if len(donations) == 0:
        print("There are no donations.")
    else:
        for donation in donations:
            print(donation)
