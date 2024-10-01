import hashlib
import maskpass

class ActiveAccount:
    def __init__(self, username, token):
        self.username = username
        self.token = token

class AuthClientRepository:
    def __init__(self):
        pass

    def getUser(self, name, passwordHash):
        return True

    def create(self, name, passwordHash):
        return True



class AuthClient:
    def __init__(self): 
        self.repo = AuthClientRepository()

    def login(self) -> ActiveAccount:
        name = input("Write your username: ")
        password = maskpass.askpass("Write your password: ")
        passwordHash = self.hash(password)

        getUser = self.repo.getUser(name, passwordHash) 

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

        creteUser = self.repo.create(name, passwordHash)
        if creteUser == True:
            user = ActiveAccount(name, passwordHash)
            return user
        else:
            return None
        return None

    def hash(self, password):
        m = hashlib.sha256()
        m.update(password.encode())
        passwordHash = m.hexdigest()
        return passwordHash


        