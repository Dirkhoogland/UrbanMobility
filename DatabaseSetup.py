import sqlite3

def Databasesetupstart():



    # functie die kijkt of de DB geen tabellen heb voor set up
    if is_database_empty():
        print("De database is leeg heeft geen tabellen.")
        createdatabase();
        print("Er zijn nieuwe tabellen aangemaakt.")
    else:
        print("De database bevat al tabellen, er worden geen nieuwe aangemaakt.")


# functie om Db te checken
def is_database_empty():
     conn = sqlite3.connect("Database.db")
     cursor = conn.cursor()

      # Query om te kijken of er tabellen zijn in de database
     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
     tables = cursor.fetchall()

     conn.close()

     # Als er geen tabellen zijn, is de database leeg.
     return len(tables) == 0



# Creates the Database
def createdatabase():
    conn = sqlite3.connect("Database.db")

    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE Users (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    rank INTEGER NOT NULL, 
    Username TEXT NOT NULL,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE Traveller(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Firstname TEXT NOT NULL,
    Lastname TEXT NOT NULL,
    Birthday TEXT NOT NULL -- ISO 8601 format: YYYY-MM-DD,
    Gender TEXT NOT NULL,
    Streetname TEXT NOT NULL,
    Housenumber INTEGER NOT NULL,
    City TEXT NOT NULL, 
    EmailAdress TEXT NOT NULL,
    MobilePhone TEXT NOT NULL,
    DrivingLiscenceNumber TEXT NOT NULL
    ) ''')

    cursor.execute(''''CREATE TABLE Scooter() 
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Brand TEXT NOT NULL,
    Model TEXT NOT NULL,
    Serialnumber NOT NULL CHECK (length(wachtwoord) BETWEEN 10 AND 17,
    TopSpeed TEXT NOT NULL,
    BatteryCapacity TEXT NOT NULL,
    Soc TEXT NOT NULL,
    TargetRangeSoC TEXT NOT NULL,
    longitude REAL NOT NULL,
    latitude  REAL NOT NULL,
    OutOfServiceStatus BOOL,
    Mileage INTERGER,
    LastMaintainanceDate TEXT NOT NULL -- ISO 8601 format: YYYY-MM-DD
    )''')


