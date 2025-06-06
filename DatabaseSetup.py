import sqlite3
import os

import Databasefunctions
import Hasher


script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.db")
def Databasesetupstart():



    # functie die kijkt of de DB geen tabellen heb voor set up
    if is_database_empty():
        print("De database is leeg heeft geen tabellen.")
        createdatabase();
        print("Er zijn nieuwe tabellen aangemaakt.")
        filldatabase();
        print("Er is data toegevoegd.")
    else:
        print("De database bevat al tabellen, er worden geen nieuwe aangemaakt.")


# functie om Db te checken
def is_database_empty():
     conn = sqlite3.connect(db_path)
     cursor = conn.cursor()

      # Query om te kijken of er tabellen zijn in de database
     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
     tables = cursor.fetchall()

     conn.close()

     # Als er geen tabellen zijn, is de database leeg.
     return len(tables) == 0


 # cities = ["Rotterdam", "Delf", "Den haag", "Schiedam", "Dordrecht", "Gouda", "Zoetermeer", "Barendrecht", "Spijkernisse", "Vlaardingen"]
# Creates the Database
def createdatabase():
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE Users (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Rank INTEGER NOT NULL, 
    Username TEXT NOT NULL,
    Password TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE Profiles (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        Firstname TEXT NOT NULL,
        Lastname TEXT NOT NULL,
        RegistrationDate TEXT NOT NULL,  -- Gebruik ISO 8601: YYYY-MM-DD
        FOREIGN KEY (UserID) REFERENCES Users(ID) ON DELETE CASCADE
    )''')

    cursor.execute('''CREATE TABLE Traveller(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Firstname TEXT NOT NULL,
    Lastname TEXT NOT NULL,
    -- ISO 8601 format: YYYY-MM-DD
    Birthday TEXT NOT NULL,
    Gender TEXT NOT NULL,
    Streetname TEXT NOT NULL,
    Housenumber INTEGER NOT NULL,
    City TEXT NOT NULL, 
    EmailAdress TEXT NOT NULL,
    MobilePhone TEXT NOT NULL,
    DrivingLiscenceNumber TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE Scooters( 
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Brand TEXT NOT NULL,
    Model TEXT NOT NULL,
    Serialnumber TEXT NOT NULL CHECK (length(Serialnumber) BETWEEN 10 AND 17),
    TopSpeed TEXT NOT NULL,
    BatteryCapacity TEXT NOT NULL,
    Soc TEXT NOT NULL,
    TargetRangeSoC TEXT NOT NULL,
    longitude REAL NOT NULL,
    latitude REAL NOT NULL,
    OutOfServiceStatus BOOLEAN,
    Mileage INTEGER,
    LastMaintainanceDate TEXT NOT NULL -- ISO 8601 format: YYYY-MM-DD
    )''')



    conn.close()


def filldatabase():

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()
    scooters = [
    ("Segway", "E110S", "SEGWAY00123", "45 km/h", "2.5 kWh", "90%", "80%", 4.89943, 52.37919, False, 1200, "2024-04-01"),
    ("NIU", "MQi+", "NIU0004567", "45 km/h", "2.0 kWh", "75%", "60%", 4.89756, 52.37315, False, 840, "2024-03-15"),
    ("SuperSoco", "CUx", "SSCUX00001", "45 km/h", "1.8 kWh", "88%", "70%", 4.90567, 52.37022, True, 1620, "2024-02-25"),
    ("Yadea", "G5", "YADEAG5002", "45 km/h", "2.2 kWh", "92%", "85%", 4.91111, 52.37789, False, 760, "2024-01-30"),
    ("Horwin", "EK3", "HORWIN0034", "45 km/h", "3.0 kWh", "81%", "72%", 4.88654, 52.36802, False, 500, "2024-05-10"),
    ]

    cursor.executemany('''
    INSERT INTO Scooters (
        Brand, Model, Serialnumber, TopSpeed, BatteryCapacity, 
        Soc, TargetRangeSoC, longitude, latitude, 
        OutOfServiceStatus, Mileage, LastMaintainanceDate
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', scooters)

    travellers = [
    ("Anna", "Jansen", "1990-05-12", "F", "Lindelaan", 23, "Rotterdam", "anna.jansen@example.com", "0612345678", "NL123456789"),
    ("Tom", "de Boer", "1985-11-03", "M", "Beukenstraat", 57, "Rotterdam", "tom.boer@example.com", "0687654321", "NL987654321"),
    ("Fatima", "El Amrani", "1998-07-25", "F", "Kastanjelaan", 11, "Rotterdam", "fatima.amrani@example.com", "0699988776", "NL112233445"),
    ]

    cursor.executemany('''
    INSERT INTO Traveller (
        Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, 
        City, EmailAdress, MobilePhone, DrivingLiscenceNumber
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', travellers)



    users = [
    (0, "super_admin", "Admin_123?"),
    (1, '_jan.01', 'S3cure#Pass!12'),
    (2, 'Mark_007', 'Strong!Pass123$')
    ]
    profiles = [
    (2, "Jan", "Jansen"),
    (3, "Mark", "Pieters")
    ]   


    for rank, username, plain_password in users:
        hashed_pw = Hasher.hash_password(plain_password)
        cursor.execute('INSERT INTO Users (Rank, Username, Password) VALUES (?, ?, ?)', (rank, username, hashed_pw))
    
    conn.commit()
    conn.close()
    for userid,firstname, lastname in profiles:
        Databasefunctions.add_profile_for_user(userid,firstname, lastname)

