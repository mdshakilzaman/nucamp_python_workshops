class User:
    '''base class for a user where is requires name, pin and password'''

    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        '''Changes the name of the user'''
        self.name = new_name

    def change_pin(self, new_pin):
        '''Changes the pin of the user'''
        self.pin = new_pin

    def change_password(self, new_password):
        '''Changes the password of the user'''
        self.password = new_password


class BankUser(User):
    '''subclass of User class. It has additional methods.'''

    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        '''Prints the BankUser object's balance'''
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, amount):
        '''Withdraws money, decreases the account balance'''
        self.balance -= amount

    def deposit(self, amount):
        '''Deposits money, increases the account balance'''
        self.balance += amount

    def transfer_money(self, amount, user2):
        '''transfer money to another user
        inputs
        amount: amount of money to transfer
        user2:another user(an object from BankUser class which the money will be transfered)
        output: boolean
        '''
        print("your are transfering $", amount, "to", user2.name)
        print("Authentication required")
        user_pin = int(input("Enter your pin: "))
        if user_pin == self.pin:
            print("Transfer authorized")
            print("transfering", amount, "to", user2.name)
            self.balance -= amount
            user2.balance += amount
            return True
        else:
            print("Invalid pin. Transaction cancelled.")
            return False

    def request_money(self, amount, user2):
        '''request money from another user
        inputs
        amount: amount of money to request
        user2:another user(an object from BankUser class which the money will be requested)
        output: boolean
        '''
        print("your are requesting $", amount, "to", user2.name)
        print("user authentication is required")
        user2_pin = int(input("Enter {}'s pin: ".format(user2.name)))
        if user2_pin != user2.pin:
            print("Invalid pin. Transaction cancelled.")
            return False
        user1_pass = input("enter your password: ")
        if user1_pass != self.password:
            print("Invalid password. Transaction cancelled.")
            return False
        if str(user1_pass) == self.password and user2_pin == user2.pin:
            print("request authorized")
            print(user2.name, "sent", amount)
            user2.balance -= amount
            self.balance += amount
            return True


if __name__ == "__main__":
    # """ Driver Code for Task 1 """
    # user1 = User(name="Bob", pin=1234, password="password")
    # print(user1.name, user1.pin, user1.password)

    # """ Driver Code for Task 2 """
    # user1.change_name("Bobby")
    # user1.change_pin(4321)
    # user1.change_password("newpassword")
    # print(user1.name, user1.pin, user1.password)

    # """ Driver Code for Task 3"""
    # banker1 = BankUser(name="Bob", pin=1234, password="password")
    # print(banker1.name, banker1.pin, banker1.password, banker1.balance)

    # """ Driver Code for Task 4"""
    # banker1 = BankUser(name="Bob", pin=1234, password="password")
    # banker1.show_balance()
    # banker1.deposit(1000)
    # banker1.show_balance()
    # banker1.withdraw(500)
    # banker1.show_balance()
    """ Driver Code for Task 5"""
    banker1 = BankUser(name="Bob", pin=1234, password="pass1")
    banker2 = BankUser(name="Alice", pin=4321, password="pass2")
    banker2.deposit(5000)
    banker2.show_balance()
    banker1.show_balance()
    banker2.transfer_money(500, banker1)
    banker2.show_balance()
    banker1.show_balance()
    banker2.request_money(250, banker1)
    banker2.show_balance()
    banker1.show_balance()
