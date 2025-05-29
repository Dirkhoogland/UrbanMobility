import sqlite3
import os
import Hasher


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

