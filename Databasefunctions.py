from datetime import date
import sqlite3
import os
from tabnanny import check
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
    cursor.execute("SELECT ID, Rank, Username FROM Users WHERE Username = ?", (Username,))
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

    speedcheck = Validator.is_valid_top_speed(Scooter[4])
    if speedcheck == False:
        print(f"Invalid speed: {Scooter[4]}")

    capacitycheck = Validator.is_valid_battery_capacity(Scooter[5])
    if capacitycheck == False:
        print(f"Invalid Battery Capacity: {Scooter[5]}")

    chargecheck = Validator.is_valid_soc(Scooter[6])
    if chargecheck == False:
        print(f"Invalid Battery Capacity: {Scooter[6]}")

    maintcheck = Validator.is_valid_maintenance_date(Scooter[12])
    if maintcheck == False:
        print(f"Invalid maintainance date: {Scooter[12]}")

    if speedcheck and capacitycheck and chargecheck and maintcheck:
        print("Waarden zijn gelidig database wordt geupdate")



        query = """
        UPDATE Scooters SET
            TopSpeed = ?,
            BatteryCapacity = ?,
            Soc = ?,
            TargetRangeSoC = ?,
            OutOfServiceStatus = ?,
            Mileage = ?,
            LastMaintainanceDate = ?
        WHERE ID = ?
        """

        values = (
        Scooter[4],
        Scooter[5],
        Scooter[6],
        Scooter[7],
        Scooter[10],
        Scooter[11],
        Scooter[12],
        Scooter[0]
        )

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()                 
        conn.close()  

# general functions
def FetchallScooter():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Scooters")
    Scooter = cursor.fetchall()
    conn.close()
    return Scooter

def passwordchange(user, pw, oldpw):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("Select Password FROM Users WHERE ID = ?", (user[0],))
    dbuser = cursor.fetchone()
    conn.close()

    stored_hash = dbuser[0]
    if Hasher.check_password(pw, stored_hash):
        print("Nieuw wachtwoord mag niet hetzelfde zijn als het oude.")
        return False


    if Hasher.check_password(oldpw, stored_hash):
        hashed_pw = Hasher.hash_password(pw)

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE Users SET Password = ? WHERE ID = ?", (hashed_pw, user[0]))
        conn.commit()                 
        conn.close()  
        print("Password updated.")

    else:
        print("Ongeldig wachtwoord.")
        return False

def add_profile_for_user(user_id, firstname, lastname):
    # Formaat: YYYY-MM-DD
    registration_date = date.today().isoformat()  

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO Profiles (UserID, Firstname, Lastname, RegistrationDate)
            VALUES (?, ?, ?, ?)
        ''', (user_id, firstname, lastname, registration_date))

        conn.commit()
        print("Profiel succesvol aangemaakt.")
    except sqlite3.Error as e:
        print(f"Fout bij aanmaken profiel: {e}")
    finally:
        conn.close()

def searchprofile(user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Profiles WHERE UserID = ?", (user_id,))
    profiel = cursor.fetchone()

    conn.close()

    if profiel:
        print("Profiel gevonden:")
        print(f"Voornaam: {profiel[2]}")
        print(f"Achternaam: {profiel[3]}")
        print(f"Registratiedatum: {profiel[4]}")
        return profiel
    else:
        print("Geen profiel gevonden voor deze gebruiker.")
        return None

def add_user(username, password, rank):

    check = check_user(username)
    if check == False:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = ON") 
        cursor = conn.cursor()
        hashed_pw = Hasher.hash_password(password)
        try:
            cursor.execute('''
               INSERT INTO Users (Rank, Username, Password )
                VALUES (?, ?, ?)
            ''', (rank, username, hashed_pw))

            conn.commit()
            print("User succesvol aangemaakt.")
        except sqlite3.Error as e:
            print(f"Fout bij aanmaken User: {e}")
            conn.close()
            return False

        conn.close()
        return True
    else:
        print("Username bestaat al")
        return False

def check_user(username):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user:

        return True
    else:

        return False
def get_user(username):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user:

        return user
    else:

        return
# Systeem admin

def CreateServiceMedewerker(username, password, firstname, lastname):
   check = add_user(username, password, 2)
   if check:
       user = get_user(username)
       if user:
            add_profile_for_user(user[0], firstname, lastname)
       else:
           print("Error creating profile, could not find user")
   return

# super admin 

def CreateSysteemAdmin(username, password, firstname, lastname):
   check = add_user(username, password, 1)
   if check:
       user = get_user(username)
       if user:
            add_profile_for_user(user[0], firstname, lastname)
       else:
           print("Error creating profile, could not find user")
   return
