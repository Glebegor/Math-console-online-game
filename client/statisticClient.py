import hashlib
import maskpass
import requests
import os
from config import globalAddress

class StatisticClient:
    def __init__(self) -> None:
        self.address = globalAddress

    def GetStats(self, name):
        response = requests.get(self.address + "/statistic/" + name)
        if response.status_code == 200:
            return response.json()
        else:
            return "Error"

