from client import Client

class Main:
    def __init__(self) -> None:
        self.client = Client()

    def run(self) -> None:
        self.client.run()



if __name__ == "__main__":
    main = Main()
    main.run()

  