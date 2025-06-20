from DatabaseSetup import Databasesetupstart, CreateBackup, CreateBackupKey, AccessPassword
import Databasefunctions
from UrbanMobility import Start
from Traveller import View, Update, AddTraveller, Delete, Add
from Menus import toon_dynamisch_menu, cityOption
from Encrypt import generate_key, get_key
from Databasefunctions import *

if __name__ == "__main__":
    print("versie 1.31") # om build te checken

    Databasesetupstart()
    Databasefunctions.Createbackupkey(2, "Testdatabase", "test")
    Start()
