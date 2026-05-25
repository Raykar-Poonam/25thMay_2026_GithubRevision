import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\aksha\\PycharmProjects\\PythonProject5\\Configuration\\config.ini")

class readconfig:

    @staticmethod
    def getEmail():
        Email = config.get("login data","email")
        return Email

    @staticmethod
    def getPassword():
        Password = config.get("login data","password")
        return Password