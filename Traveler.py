import sqlite3
import os
import Hasher
import Validator

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.db")

def Add(Firstname, Lastname, Birthday, Gender, Streetname, 
        Housenumber, City, EmailAdress, MobilePhone, DrivingLiscenceNumber):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    traveller = [
        (Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, City, EmailAdress, MobilePhone, DrivingLiscenceNumber)
    ]
    cursor.executemany(''''
    INSERT INTO Traveller (
        Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, 
        City, EmailAdress, MobilePhone, DrivingLiscenceNumber
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', traveller)



    # INSERT INTO Traveller (
    #     Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, 
    #     City, EmailAdress, MobilePhone, DrivingLiscenceNumber
    # ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    # ''', travellers)
    