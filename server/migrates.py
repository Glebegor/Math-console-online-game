import os

migratesFolder = "./schema/"

def migratesFromSql(filename, arg: str):
    if arg == "up": 
        file = open(migratesFolder + "000001_init.up.sql", "r")
        sql = file.read()
        file.close()
        os.system(f"sqlite3 {filename} '{sql}'")

    elif arg == "down":
        file = open(migratesFolder + "000001_init.down.sql", "r")
        sql = file.read()
        file.close()
        os.system(f"sqlite3 {filename} '{sql}'")

if __name__ == "__main__":
    migratesFromSql("./main.db", os.sys.argv[1])