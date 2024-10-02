from statistic import Statistic
from SmbolicImages import gigachad, myaw, frog
from authClient import AuthClient, ActiveAccount
import os

class Client:
    def __init__(self) -> None:
        self.stats = Statistic()
        self.authClient = AuthClient()
        self.activeAccountUser = None
        self.root = False


    def run(self) -> None:

        os.system("clear")
        print(gigachad.img)
        print("|#################################################|")
        print("|#                                               #|")
        print("|#               -running client-                #|")
        print("|#                                               #|")
        print("|#################################################|")

        print("|#-----Welcome to the client!-----#")
        print("|# 1. Yes")
        print("|# 2. No")

        choise = input("|# Do you wanna play a math game? ")
        if choise == "1":
            os.system('clear')
            self.auth()
        else:
            self.goodbye()

        

    def lobby(self) -> None:
        os.system('clear')
        print("|#################################################|")
        print("|#                                               #|")
        print("|#                   -lobby-                     #|")
        print("|#                                               #|")
        print("|#################################################|")
        print("|#---Lobby---#")
        print("|# 1. Play game")
        print("|# 2. Show statistics")
        print("|# 3. Logout")
        print("|# 4. Exit")
        print("|#---Lobby---#")
        choise = input("|# Write the number of the action you want to do: ")

        if choise == "1":
            pass
        elif choise == "2":
            pass
        elif choise == "3":
            os.system('clear')
            self.activeAccountUser = None
            self.auth()
            return
        elif choise == "4":
            self.goodbye()
        elif choise == "secret":
            os.system('clear')
            print(frog.img)
            self.root = True
            input("Press enter to continue...")
            self.lobby()
        else:
            print("Invalid input.")
            self.lobby()


    def activeAccount(self) -> bool:
        os.system('clear')
        with open("./accounts_tokens/tokens.txt", "r") as f:
            tokens = f.readlines()
            if len(tokens) != 0:
                print("|################")
                for i, token in enumerate(tokens):
                    print(f"|# {i+1}. {token.split(":")[0]} - {token.split(":")[1]}".strip()[:50] + "...")
                print("|#---Accounts---#")
                print("|# 1. Login/Register other account")
                print("|# 2. Delete account")
                choise = input("|# You have saved accounts. Write id of the account to login: ")
                if choise == "1" or choise == "":
                    return False
                elif choise == "2":
                    choise = input("Write id of the account you want to delete: ")
                    choise = int(choise)
                    del tokens[choise-1]
                    with open("./accounts_tokens/tokens.txt", "w") as f:
                        f.writelines(tokens)
                    self.messageSuccess("Account deleted.")
                    return False
                else:
                    try:
                        int(choise)
                    except:
                        return self.activeAccount()
                    choise = int(choise)
                    e = self.authClient.checkUser(tokens[choise-1].split(":")[0], tokens[choise-1].split(":")[1].strip())
                    if e == True:
                        self.activeAccountUser = ActiveAccount(tokens[choise-1].split(":")[0], tokens[choise-1].split(":")[1])
                        self.messageSuccess("You are logged in as: " + self.activeAccountUser.username)
                        return True
                    else:
                        self.messageError("Invalid username or token.")
                        return False
            else:
                return False

    def auth(self) -> None:
        if self.activeAccount():
            self.lobby()
            return
        
        os.system('clear')
        print("|#################################################|")
        print("|# 1. Login")
        print("|# 2. Register")
        print("|# Do you want to login or register? (n to exit): ")
        choise = input()
        if choise == "1":
            e = self.authClient.login()
            if e != None:
                self.activeAccountUser = e
                self.addToken()
                self.messageSuccess("You are logged in as: " + self.activeAccountUser.username)
                self.lobby()
                return
            else:
                self.messageError("Invalid username or password.")
                self.auth()
                return
        elif choise == "2":
            e = self.authClient.register()
            if e != None:
                self.activeAccountUser = e
                self.addToken()
                self.messageSuccess("You are registered as: " + self.activeAccountUser.username)
                self.lobby()
                return
            else:
                self.messageError("Username already exists.")
                self.auth()
            return
        elif choise == "n":
            self.goodbye()
        else:
            print("Invalid input.")
            self.auth()
            return
        
    def addToken(self) -> None:
        for i in open("./accounts_tokens/tokens.txt", "r").readlines():
            if i.split(":")[0] == self.activeAccountUser.username:
                return

        with open("./accounts_tokens/tokens.txt", "a") as f:
            f.write(f"{self.activeAccountUser.username}:{self.activeAccountUser.token}\n")
              
    def messageSuccess(self, message: str) -> None:
        os.system('clear')
        print("|--------------!! Success !!-------------#")
        print(f"| Success: {message}")
        print("|----------------------------------------#")


    def messageError(self, message: str) -> None:
        os.system('clear')
        print("|--------------!! Error !!-------------#")
        print(f"| Error: {message}")
        print("|--------------------------------------#")

    def goodbye(self) -> None:
        os.system('clear')
        print(myaw.img)
        print("|# ------- Goodbye! ------- #|")
        exit()