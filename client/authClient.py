import hashlib
import maskpass
import requests

class ActiveAccount:
    def __init__(self, username, token):
        self.username = username
        self.token = token

class AuthClientService:
    def __init__(self):
        self.address = "http://127.0.0.1:5000"

    def login(self, name, passwordHash):
        # json request
        response = requests.post(self.address + "/login", json={"username": name, "password": passwordHash})
        if response.status_code == 200:
            if response.json()['message'] == "Success":
                return True
            else:
                return False
        else:
            return False
        

    def register(self, name, passwordHash):
        # json request
        response = requests.post(self.address + "/register", json={"username": name, "password": passwordHash})
        if response.status_code == 200:
            if response.json()['message'] == "Success":
                return True
            else:
                return False
        else:
            return False
        
 


class AuthClient:
    def __init__(self): 
        self.service = AuthClientService()

    def login(self) -> ActiveAccount:
        name = input("Write your username: ")
        password = maskpass.askpass("Write your password: ")
        passwordHash = self.hash(password)

        getUser = self.service.login(name, passwordHash) 

        if getUser == True:
            user = ActiveAccount(name, passwordHash)
            return user
        else:
            return None
        return None

    def register(self) -> ActiveAccount:
        name = input("Write your username: ")
        password = maskpass.askpass("Write your password: ")
        passwordHash = self.hash(password)

        creteUser = self.service.register(name, passwordHash)
        if creteUser == True:
            user = ActiveAccount(name, passwordHash)
            return user
        else:
            return None
        return None
    
    def checkUser(self, name, passwordHash):
        getUser = self.service.login(name, passwordHash)
        if getUser == True:
            return True
        else:
            return False

    def hash(self, password):
        m = hashlib.sha256()
        m.update(password.encode())
        passwordHash = m.hexdigest()
        return passwordHash


        