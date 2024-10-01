from statistic import Statistic
from SmbolicImages import gigachad, myaw
from authClient import AuthClient, ActiveAccount

class Client:
    def __init__(self) -> None:
        self.stats = Statistic()
        self.authClient = AuthClient()
        self.activeAccountUser = None


    def run(self) -> None:
        print(gigachad.img)
        print("|--------------------------------------------|")
        print("|############################################|")
        print("|# Running client...                        #|")
        print("|############################################|")
        print("|--------------------------------------------|")

        print("Welcome to the client!")
        choise = input("Do you wanna play a math game? (y/n) ")
        if choise == "y":
            self.auth()
        else:
            print(myaw.img)
            print("Goodbye!")
            exit()

    def activeAccount(self) -> bool:
        with open("./accounts_tokens/tokens.txt", "r") as f:
            tokens = f.readlines()
            if len(tokens) != 0:
                print("#---Accounts---#")
                for i, token in enumerate(tokens):
                    print(f"{i+1}. {token.split(":")[0]} - {token.split(":")[1]}".strip())
                print("#---Accounts---#")

                choise = input("You have saved accounts. Write id of the account if you wanna use them (write n if you want to leave, d if you want to delete acc.): ")
                if choise == "n":
                    return False
                elif choise == "d":
                    choise = input("Write id of the account you want to delete: ")
                    choise = int(choise)
                    del tokens[choise-1]
                    with open("./accounts_tokens/tokens.txt", "w") as f:
                        f.writelines(tokens)
                    return False
                else:
                    choise = int(choise)
                    self.activeAccountUser = ActiveAccount(tokens[choise-1].split(":")[0], tokens[choise-1].split(":")[1])
                    return True
            else:
                return False

    def auth(self) -> None:
        if self.activeAccount():
            print("You are logged in as:", self.activeAccountUser.username)
            return

        print("You want to login or register? (l/r): ")
        choise = input()
        if choise == "l":
            self.authClient.login()
        elif choise == "r":
            self.authClient.register()
            pass
        else:
            print("Invalid input.")
            self.auth()
            