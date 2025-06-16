from DatabaseSetup import Databasesetupstart, CreateBackup
from UrbanMobility import Start
from Traveller import View, Update, AddTraveller
from Menus import toon_dynamisch_menu, cityOption
from Encrypt import generate_key

if __name__ == "__main__":
    Databasesetupstart()
    CreateBackup()
    # print(View("anna.jansen@example.com"))
    # gAAAAABoTrJ0xX8UECoPz3IgwzsAHeo4RyxZE1eD9qgU1TBf7rE8DA9wVUE6055FQLXtHfZ6Shf9NNILpzHZRChmDP4QRVJTBMxUkNyRT8SdAreWA8J7HeA=

    print("versie 1.24") # om build te checken
    # Databasesetupstart()
    # # Update("anna.jansen@example.com")

    # print("versie 1.20") # om build te checken

    Start()