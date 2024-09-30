from statistic import Statistic
from SmbolicImages import gigachad, myaw

class Client:
    def __init__(self) -> None:
        self.stats = Statistic()

    def Register(self):
        self.stats.service.register()

    def Login(self):
        self.stats.service.login()

    def run(self) -> None:
        print(gigachad.img)
        print("|--------------------------------------------|")
        print("|############################################|")
        print("|# Running client...                        #|")
        print("|############################################|")
        print("|--------------------------------------------|")

        print("Welcome to the client!")
        choise = input("Do you wanna play a game? (y/n) ")
        if choise == "y":
            self.auth()
        else:
            print(myaw.img)
            print("Goodbye!")
            exit()

    def auth(self):
        print("You want to login or register? (l/r): ")
        choise = input()
        if choise == "l":
            self.Login()
        elif choise == "r":
            self.Register()
        else:
            print("Invalid input")
            self.auth()
            