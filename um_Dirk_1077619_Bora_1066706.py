from DatabaseSetup import Databasesetupstart
from UrbanMobility import Start
from Traveller import View, Update, AddTraveller
from Menus import toon_dynamisch_menu, cityOption

if __name__ == "__main__":
    print("versie 1.13") # om build te checken
    Databasesetupstart()
    Update("anna.jansen@example.com")
    Start()