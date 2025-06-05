from DatabaseSetup import Databasesetupstart
from UrbanMobility import Start
from Traveler import View, Update

if __name__ == "__main__":
    View("anna.jansen@example.com") # used for testing assing this behind roles
    print("versie 1.7") # om build te checken
    Update("anna.jansen@example.com") # used for testing assing this behind roles
    Databasesetupstart()
    Start()