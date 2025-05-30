import sqlite3
import os
import Hasher
import Validator

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.db")

def login(Username, Password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = ?", (Username,))
    user = cursor.fetchone()
    
    conn.close()

    if user is None:
        print("Gebruiker niet gevonden.")
        return False

    stored_hash = user[3]  

    if Hasher.check_password(Password, stored_hash):
        print("Inloggen gelukt!")
        return True
    else:
        print("Ongeldig wachtwoord.")
        return False
    
# krijgt de user gegevens bij inlog
def getuserdetails(Username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT Rank, Username FROM Users WHERE Username = ?", (Username,))
    user = cursor.fetchone()
    conn.close()
    return user




# scooter functies Service

def GetScooterService(Serialnumber):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Scooters WHERE Serialnumber = ?", (Serialnumber,))
    Scooter = cursor.fetchone()
    conn.close()
    return Scooter

def Scooterupdate(Scooter):

    speedcheck = Validator.is_valid_top_speed(Scooter[3])
    if speedcheck == False:
        print(f"Invalid speed: {Scooter[3]}")

    capacitycheck = Validator.is_valid_battery_capacity(Scooter[4])
    if capacitycheck == False:
        print(f"Invalid Battery Capacity: {Scooter[4]}")




    if speed != " ":
        Scooter[3] = speed
    if capacity != " ":
        Scooter[4] = capacity
    if charge != " ":
        Scooter[5] = charge
    if Trs != " ":
        Scooter[6] = Trs
    if location != " ":
        Scooter[7] = location
    if outofservice != " ":
        Scooter[8] = outofservice
    if milage != " ":
        Scooter[9] = milage
    if lastmain != " ":
        Scooter[10] = lastmain