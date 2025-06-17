from DatabaseSetup import Databasesetupstart, CreateBackup, CreateBackupKey, AccessPassword
from UrbanMobility import Start
from Traveller import View, Update, AddTraveller, Delete, Add
from Menus import toon_dynamisch_menu, cityOption
from Encrypt import generate_key

if __name__ == "__main__":
    print("versie 1.27") # om build te checken
    # while True:
    #     if AccessPassword():
    #         CreateBackup()
    # print(View("anna.jansen@example.com"))

    Databasesetupstart()
    # Update("anna.jansen@example.com")
    Delete("anna.jansen@example.com")
    Add("Anna", "Jansen", "1990-05-12", "F", "Lindelaan", 23, "1234AB", "Rotterdam", "anna.jansen@example.com", "+31-6-06123456", "NL1234567") # add Anna back for testing purposes