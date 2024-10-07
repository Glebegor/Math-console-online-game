from config import globalAddress
import requests

class GameClient:
    def __init__(self) -> None:
        self.address = globalAddress

    def GetGames(self):
        response = requests.get(self.address + "/rooms")
        if response.status_code == 200 :
            return response.json()
        else:
            return "Error"

    def CreateGame(self):
        pass