from DatabaseSetup import Databasesetupstart, CreateBackup, CreateBackupKey, AccessPassword
from UrbanMobility import Start
from Traveller import View, Update, AddTraveller
from Menus import toon_dynamisch_menu, cityOption
from Encrypt import generate_key

if __name__ == "__main__":
    print("versie 1.26") # om build te checken
    # while True:
    #     if AccessPassword():
    #         CreateBackup()
    # print(View("anna.jansen@example.com"))

    Databasesetupstart()
    Update("anna.jansen@example.com")

    # print("versie 1.20") # om build te checken

    Start()