from DatabaseSetup import Databasesetupstart
from UrbanMobility import Start
from Traveler import View, Update, AddTraveller

if __name__ == "__main__":
    print("versie 1.9") # om build te checken
    AddTraveller()
    Update("anna.jansen@example.com") # used for testing assing this behind roles
    Databasesetupstart()
    Start()