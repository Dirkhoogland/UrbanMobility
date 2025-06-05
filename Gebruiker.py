import sqlite3
import os
import Hasher
import Validator

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.db")

def UpdatePassword(user):
    OldPassword = input("Oude Wachtwoord: ")
    NewPassword = input("Niuewe Wachtwoord: ")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = ?", (user))
    user = cursor.fetchone()

    conn.close()