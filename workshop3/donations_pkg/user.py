def login(database, username, password):
    # key = list(database.keys())[0]
    # value = list(database.values())[0]
    if username in database:
        if database[username] == password:
            print("welcome to DonateMe!")
            return username
        else:
            print("incorrect password for admin.")
            return []
    else:
        print("username not found! please register.")
        return []


def register(database, username):
    if username in database:
        print("username already exists.")
        return ""
    else:
        print(username, "has been registered.")
        return username
