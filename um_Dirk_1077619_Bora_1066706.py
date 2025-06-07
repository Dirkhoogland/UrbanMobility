from DatabaseSetup import Databasesetupstart
from UrbanMobility import Start
from Traveler import View, Update, AddTraveller

if __name__ == "__main__":
    Databasesetupstart()
    print("versie 1.11") # om build te checken
    Start()