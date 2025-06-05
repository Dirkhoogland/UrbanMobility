import sqlite3
import os
import Hasher
import Validator
import datetime
from Menus import toon_dynamisch_menu, TravelerUpdateOptions

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.db")

def View(Email):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Traveller WHERE EmailAdress = ?
    ''', (Email,))
    target = cursor.fetchone()
    print(target)
    conn.commit()
    conn.close()

def Add(Firstname, Lastname, Birthday, Gender, Streetname, 
        Housenumber, City, EmailAdress, MobilePhone, DrivingLiscenceNumber):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    traveller = [
        (Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, City, EmailAdress, MobilePhone, DrivingLiscenceNumber)
    ]
    cursor.executemany('''
    INSERT INTO Traveller (
        Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, 
        City, EmailAdress, MobilePhone, DrivingLiscenceNumber
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', traveller)
    conn.close()

def Update(Email):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("what do you want to update?")
    print()
    toon_dynamisch_menu(TravelerUpdateOptions(), "Traveller Update Menu")
    while True:
        option = int(input("Select option: "))
        if option == 1:
            Newfirstname = ""
            while Newfirstname == "":
                Newfirstname = str(input("New Firstname: "))
            conn.execute('''
                UPDATE traveller SET Firstname = ? WHERE EmailAdress = ?
            ''', (Newfirstname, Email,))
            print("Update on Firstname Succesfull")
            conn.commit()

        if option == 2:
            Newlastname = ""
            while Newlastname == "":
                Newlastname = str(input("New Lastname: "))
            conn.execute('''
                UPDATE traveller SET Lastname = ? WHERE EmailAdress = ?
            ''', (Newlastname, Email))

            print("Update on Lastname Succesfull")
            conn.commit()

        if option == 3:
            while True:
                try:
                    Newbirthday = input("New Birthday (yyyy-mm-dd):")
                    frag = Newbirthday.split('-')

                    if len(frag) != 3:
                        print("Wrong format used, use the following format: (2025-01-01)")
                        continue

                    year = int(frag[0]) 
                    month = int(frag[1])
                    day = int(frag[2])
                    parsed_date = datetime.datetime.strptime(year, month, day, "%Y-%m-%d").date() # used to check if date is valid
                    
                except:
                    print("wrong format used, use fellowing format: (2025-01-01)")

        if option == 4:
            pass
        if option == 5:
            pass
        if option == 6:
            pass
        if option == 7:
            pass
        if option == 8:
            conn.close()
            break
    

    # INSERT INTO Traveller (
    #     Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, 
    #     City, EmailAdress, MobilePhone, DrivingLiscenceNumber
    # ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    # ''', travellers)
    