from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

if __name__ == '__main__':
    database = {"admin": "password123"}
    donations = []
    authorized_user = ""
    show_homepage()
    if len(authorized_user) == 0:
        print("You must be logged in to donate.")
    else:
        print("Logged in as ", authorized_user)

    while True:
        user_input = input("choose an option: ")
        if user_input == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            authorized_user = login(database, username, password)
            if len(authorized_user) != 0:
                print("welcome back", authorized_user, "!")
                show_homepage()
                print("Logged in as:", authorized_user)
        if user_input == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            authorized_user = register(database, username)
            if len(authorized_user) != 0:
                database[username] = password

        if user_input == '3':
            if len(authorized_user) == 0:
                print("You are not logged in!")
            else:
                donation_string = donate(authorized_user)
                donations.append(donation_string)
        if user_input == '4':
            show_donations(donations)
        if user_input == '5':
            print("5: Leaving DonateMe...!")
            break
