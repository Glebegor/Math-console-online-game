from SmbolicImages import gigachad, myaw, frog
from authClient import AuthClient, ActiveAccount
from statisticClient import StatisticClient
from gameClient import GameClient
import os

class Client:
    def __init__(self) -> None:
        self.authClient = AuthClient()
        self.statisticClient = StatisticClient()
        self.GameClient = GameClient()
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
            os.system('clear')
            print("|#################################################|")
            print("|#                                               #|")
            print("|#                 -Math game-                   #|")
            print("|#                                               #|")
            print("|#################################################|")
            print("|#---Math Game---#")
            print("|# 1. Search game")
            print("|# 2. Create game")
            print("|# 3. Back")
            print("|#---Math Game---#")
            localChoise = input("|# Write the number of the action you want to do: ")
            if localChoise == "1":               
                games = self.GameClient.GetGames()
            elif localChoise == "2":
                game = self.GameClient.CreateGame()
            elif localChoise == "3":
                self.lobby()
                return

        elif choise == "2":
            os.system('clear')
            stats = self.statisticClient.GetStats(self.activeAccountUser.username)
            print("|#---Statistics---#")
            if stats == "Error":
                print("|# Error while getting statistics.")
            else:
                print("|# Statistics for: " + self.activeAccountUser.username)
                if stats['count_of_games'] == 0:
                    print("|# Win rate: " + "-%")
                else:
                    print("|# Win rate: " + round(stats['count_of_wins']/stats['count_of_games']) + "%")
                print("|# Total games: " + str(stats['count_of_games']))
                print("|# Total wins: " + str(stats['count_of_wins']))
                print("|# Total loses: " + str(stats['count_of_loses']))
                print("|# Biggest streak: " + str(stats['bigger_win_streak']))
                print("|# Win streak: " + str(stats['win_streak']))
                print("|# Biggest number: " + str(stats['biggest_number']))
                print("|# Rating: " + str(stats['rating']))
            print("|#---Statistics---#")
            input("Press enter to continue...")
            self.lobby()
            return
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
            return
        else:
            print("Invalid input.")
            self.lobby()
            return


    def activeAccount(self) -> bool:
        os.system('clear')
        with open("./accounts_tokens/tokens.txt", "r") as f:
            tokens = f.readlines()
            if len(tokens) != 0:
                print("|################")
                for i, token in enumerate(tokens):
                    print(f"|# {i+1}. {token.split(":")[0]} - {token.split(":")[1]}".strip()[:50] + "...")
                print("|#---Accounts---#")
                print("|# a. Login/Register other account")
                print("|# b. Delete account")
                choise = input("|# You have saved accounts. Write id of the account to login: ")
                if choise == "a" or choise == "":
                    return False
                elif choise == "b":
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
                input("Press enter to continue...")
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
                input("Press enter to continue...")
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