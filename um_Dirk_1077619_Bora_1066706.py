from DatabaseSetup import Databasesetupstart
from UrbanMobility import Start
from Traveller import View, Update, AddTraveller
from Menus import toon_dynamisch_menu, cityOption

if __name__ == "__main__":
    Update("anna.jansen@example.com")
    Databasesetupstart()
    print("versie 1.11") # om build te checken
    Start()