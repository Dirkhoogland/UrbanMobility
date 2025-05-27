import sqlite3

# Creates the Database
def createdatabase():
    conn = sqlite3.connect("Database.db")

    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE Users (Id INTEGER PRIMARY KEY AUTOINCREMENT,
    rank TEXT, 
    Username TEXT,
    Email TEXT,
    Password TEXT)''')

    cursor.execute('''CREATE TABLE Traveller(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Firstname TEXT,
    Lastname TEXT,
    Birthday TEXT  -- ISO 8601 format: YYYY-MM-DD,
    Gender TEXT,
    Streetname TEXT,
    Housenumber INTEGER,
    City TEXT, 
    EmailAdress TEXT,

    ) ''')


    #birthday = date(1990, 7, 21).isoformat()
    #cursor.execute("INSERT INTO people (name, birthday) VALUES (?, ?)", ("Alice", birthday))
