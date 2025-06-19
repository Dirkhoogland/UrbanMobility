from asyncio.windows_events import NULL
from datetime import date, datetime, timedelta
import sqlite3
import os
from tabnanny import check
from typing import KeysView
import Hasher
import Validator, Menus
from Encrypt import Profiles_encrypt, Usersname_encrypt, encrypt_message, Users_encrypt, key_encrypt, profilename_encrypt
from Decrypt import Profiles_decrypt, Userdetailsdecrypt, decrypt_message
from logger import Decrypte_all_logs, Log_decrypt_many

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.db")

def aantal_gefaalde_logins(user_id, minuten=10):
 try:
    tijd_grens = datetime.now() - timedelta(minutes=minuten)
    tijd_grens_str = tijd_grens.isoformat(timespec='seconds')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT COUNT(*) FROM ActionLog
        WHERE UserID = ?
        AND Action = 'Login poging'
        AND Result = 'Ongeldig wachtwoord'
        AND Timestamp >= ?
    ''', (user_id, tijd_grens_str))
    
    aantal = cursor.fetchone()[0]
    conn.close()
    return aantal
 except sqlite3.Error as e:
        print(f"Database error: {e}")

def login(Username, Password):
 try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    conn.close()
    max_pogingen = 3
    pogingen = 0
    found = None

    for user in users:
        if(decrypt_message(user[2]) == Username):
            user_list = list(user)              # converteer naar lijst
            user_list[2] = decrypt_message(user[2])  # pas aan
            found = user_list
            break

        if pogingen >= max_pogingen:
            print("Too many attempts try again later.")
            log_actie("Login geblokkeerd", user, "Te veel pogingen", "High", "Yes")
            return False
    
    if found is None:
        log_actie("Login poging", "Gebruiker niet gevonden")
        print("user not found.")
        pogingen += 1
        return False


    stored_hash = user[3]
    if Hasher.check_password(Password, stored_hash):
        log_actie("Login poging", found, result="Succesvol")
        print("Login successful!")
        return found
    else:
        log_actie("Login poging", user, result="Ongeldig wachtwoord")
        print("invalid password.")
        pogingen += 1
        return False
 except sqlite3.Error as e:
        print(f"Database error: {e}")
    


# krijgt de user gegevens bij inlog
def getuserdetails(Username):
 try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Rank, Username FROM Users WHERE Username = ?", (Username,))
    user = cursor.fetchone()
    conn.close()
    return user
 except sqlite3.Error as e:
        print(f"Database error: {e}")
        return

def log_actie(action, user, result="", severity = "None", sus = "No"):
 try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if user == NULL:
        user[0] = 0
        user[2] = "login attempt"
    timestamp = datetime.now().isoformat(timespec='seconds')
    
    cursor.execute('''
        INSERT INTO ActionLog (Action, UserID, Username, Timestamp, Result, Severity, Suspiscious)
        VALUES (?, ?, ?, ?, ? , ?, ? )
    ''', (encrypt_message(action), user[0], encrypt_message(user[2]), encrypt_message(timestamp), encrypt_message(result), encrypt_message(severity), encrypt_message(sus))
    )
    conn.commit()
    conn.close()
 except sqlite3.Error as e:
        print(f"Database error: {e}")

def logs():
    opties = []
    logs = Decrypte_all_logs()

    for log in logs:
        optie = (
            f" Action: {log[1]} | "
            f"UserID: {log[2]} | Username: {log[3]} | "
            f"Timestamp: {log[4]} | Result: {log[5]} | "
            f"Severity: {log[6]} | Suspicious: {log[7]}"
        )
        opties.append(optie)
    
    Menus.toon_dynamisch_menu(opties, "Logs")
    input( "Press enter to continue . . .")
def StateofChargeupdate(soc, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE scooter
            SET Soc = ?
            WHERE SerialNumber = ?
        ''', (soc, Serialnumber))

        conn.commit()
        print("State of Charge edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')
    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')
def brand(brand, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE Scooters
            SET Brand = ?
            WHERE SerialNumber = ?
        ''', (brand, Serialnumber))

        conn.commit()
        print("Brand edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')
    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')
def model(model, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE Scooters
            SET Model = ?
            WHERE SerialNumber = ?
        ''', (model, Serialnumber))

        conn.commit()
        print("Model edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')

    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')
def Serialnumber(ser, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE Scooters
            SET SerialNumber = ?
            WHERE SerialNumber = ?
        ''', (ser, Serialnumber))

        conn.commit()
        print("Serialnumber edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')

    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')
def Speed(ser, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE Scooters
            SET TopSpeed = ?
            WHERE SerialNumber = ?
        ''', (ser, Serialnumber))

        conn.commit()
        print("Top speed edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')

    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')
def Battery(ser, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE Scooters
            SET BatteryCapacity = ?
            WHERE SerialNumber = ?
        ''', (ser, Serialnumber))

        conn.commit()
        print("BatteryCapacity edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')

    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')
def Milage(mil, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE Scooters
            SET Mileage = ?
            WHERE SerialNumber = ?
        ''', (mil, Serialnumber))

        conn.commit()
        print("Milage edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')
    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')
def targetrangeupdate(rnge, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE Scooters
            SET TargetRangeSoC = ?
            WHERE SerialNumber = ?
        ''', (rnge, Serialnumber))

        conn.commit()
        print("Target range edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')
    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')
def OutOfService(service, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE Scooters
            SET OutOfServiceStatus = ?
            WHERE SerialNumber = ?
        ''', (service, Serialnumber))

        conn.commit()
        print("out of service status edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')
    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')
def LocationUpdate(lat, long, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        latlong_str = f"{lat},{long}"
        cursor.execute('''
            UPDATE Scooters
            SET Location = ?
            WHERE SerialNumber = ?
        ''', (latlong_str, Serialnumber))

        conn.commit()
        print("Location edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')
    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')
def maintdate(date, Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE Scooters
            SET LastMaintainanceDate = ?
            WHERE SerialNumber = ?
        ''', (date, Serialnumber))

        conn.commit()
        print("date edited.")
        conn.close()
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {Serialnumber}", user, 'sucess', 'normal')
    except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Serialnumber}", user, 'fail', 'error')

def GetScooterService(Serialnumber):
 try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Scooters WHERE Serialnumber = ?", (Serialnumber,))
    Scooter = cursor.fetchone()
    conn.close()
    return Scooter
 except sqlite3.Error as e:
        print(f"Database error: {e}")

def ScooterupdateAdmin(scooter, user):
   try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Scooters
            SET Brand = ?, Model = ?, SerialNumber = ?, TopSpeed = ?, BatteryCapacity = ?, 
                Soc = ?, TargetRange = ?, OutOfService = ?, Milage = ?, LastMaintenance = ?
            WHERE ID = ?
        """, (
            scooter[1],  
            scooter[2],  
            scooter[3],  
            scooter[4], 
            scooter[5],  
            scooter[6],  
            scooter[7],  
            scooter[10], 
            scooter[11], 
            scooter[12], 
            scooter[0]   
        ))
        conn.commit() 
        conn.close()  
        log_actie(f"{user[2]} successfully updated a scooter with SerialNumber {scooter[3]}", user, 'sucess', 'normal')
   except sqlite3.Error as e:
        print(f"Error with updating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {scooter[3]}", user, 'fail', 'error')
   finally:
        return

def Scooterupdate(Scooter, user):
    try:
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
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Scooter[3]}", user, 'fail', 'error')
    except sqlite3.Error as e:
        print(f"Error with creating scooter: {e}")
        log_actie(f"{user[2]} failed to updating a scooter with SerialNumber {Scooter[3]}", user, 'fail', 'error')
    finally:
        return

def CreateScooter(scooter_data, user):
 try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
 
    cursor.execute('''
    INSERT INTO Scooters (
        Brand, Model, SerialNumber, TopSpeed, BatteryCapacity,
        Soc, TargetRange, OutOfService, Milage, LastMaintenance
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
    scooter_data['Brand'],
    scooter_data['Model'],
    scooter_data['SerialNumber'],
    scooter_data['TopSpeed'],
    scooter_data['BatteryCapacity'],
    scooter_data['Soc'],
    scooter_data['TargetRange'],
    scooter_data['OutOfService'],
    scooter_data['Milage'],
    scooter_data['LastMaintenance']
    ))

    conn.commit()                 
    conn.close() 
    log_actie(f" {user[2]} successfully  created a scooter with SerialNumber  {scooter_data['SerialNumber']}", user, 'success', 'normal')
 except sqlite3.Error as e:
        print(f"Error with creating scooter: {e}")
        log_actie(f"{user[2]} failed to create a scooter with SerialNumber {scooter_data['SerialNumber']}", user, 'fail', 'error')
 finally:
    return

def DeleteScooter(Serialnumber, user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Optioneel: controleer of de scooter bestaat
        cursor.execute("SELECT * FROM Scooters WHERE SerialNumber = ?", (Serialnumber,))
        scooter = cursor.fetchone()
        if not scooter:
            print("no scooter found.")
            log_actie(f" {user[2]} failed to  removed a scooter with SerialNumber  {Serialnumber} as it doesnt exist", user, 'fail', 'error')
            return False

        # Verwijder de scooter
        cursor.execute("DELETE FROM Scooters WHERE SerialNumber = ?", (Serialnumber,))
        conn.commit()
        print("Scooter removed.")
        conn.close()
        log_actie(f" {user[2]} successfully  removed a scooter with SerialNumber  {Serialnumber}", user, 'success', 'normal')
        return True

    except sqlite3.Error as e:
        print("error with revmoing scooter:", e)
        log_actie(f" {user[2]} failed to  removed a scooter with SerialNumber  {Serialnumber}", user, 'fail', 'error')
        return False

    finally:
        conn.close()
# general functions
def FetchallScooter():
 try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Scooters")
    Scooter = cursor.fetchall()
    conn.close()
    return Scooter
 except sqlite3.Error as e:
        print(f"Database error: {e}")

def passwordchange(user, pw, oldpw):
 try:
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
            log_actie(f" {user[2]} successfully  updated their password", user, 'success', 'normal')
    else:
        print("invalid password.")
        return False
 except sqlite3.Error as e:
   
            log_actie(f"{user[2]} failed to update their password", user, 'fail', 'error')
 finally:
  return


def add_profile_for_user(user_id, firstname, lastname, user):
 try:
    # Formaat: YYYY-MM-DD
   registration_date = date.today().isoformat()  
   user_info = [user_id, firstname, lastname]
   profile = Profiles_encrypt(user_info)
   conn = sqlite3.connect(db_path)
   conn.execute("PRAGMA foreign_keys = ON") 
   cursor = conn.cursor()


   cursor.execute('''
            INSERT INTO Profiles (UserID, Firstname, Lastname, RegistrationDate)
            VALUES (?, ?, ?, ?)
        ''', (user_id, profile[1], profile[2], registration_date))

   conn.commit()
   conn.close()
   print("Profiel succesvol aangemaakt.")
   log_actie(f" {user[2]} successfully  created a profile for {user_id}", user, 'success', 'normal')
 except sqlite3.Error as e:
        print(f"Fout bij aanmaken profiel: {e}")
        log_actie(f"Systeem admin {user[2]} failed to create a profile for {user_id}", user, 'fail', 'error')
 finally:
        return

def setup_add_profile_for_user(user_id, firstname, lastname):
    # Formaat: YYYY-MM-DD
    registration_date = date.today().isoformat()  
    user_info = [user_id, firstname, lastname]
    profile = Profiles_encrypt(user_info)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO Profiles (UserID, Firstname, Lastname, RegistrationDate)
            VALUES (?, ?, ?, ?)
        ''', (user_id, profile[1], profile[2], registration_date))

        conn.commit()
        conn.close()

      
    except sqlite3.Error as e:
        print(f"error with making profile in setup: {e}")
        
    finally:
        return
def searchprofile(user_id):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Profiles WHERE UserID = ?", (user_id,))
    profiel = cursor.fetchone()

    conn.close()

    if profiel:
        profiel = Profiles_decrypt(profiel)
        return profiel
    else:
        print("Geen profiel gevonden voor deze gebruiker.")
        return None

def add_user(username, password, rank, user):
 try:
    check = check_user(username)
    if check == False:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = ON") 
        cursor = conn.cursor()
        hashed_pw = Hasher.hash_password(password)

        usere = Usersname_encrypt(username)
        try:
            cursor.execute('''
               INSERT INTO Users (Rank, Username, Password )
                VALUES (?, ?, ?)
            ''', (rank, usere, hashed_pw))

            conn.commit()
            conn.close()
            print("User succesvol aangemaakt.")
            log_actie(f"{user[2]} successfully created account for {username}", user, 'success', 'normal')
       
        except sqlite3.Error as e:
            print(f"Fout bij aanmaken User: {e}")
            log_actie(f"{user[2]} failed to create account for {username}", user, 'fail', 'error')
            return False


        return True
    else:
        print("Username bestaat al")
        log_actie(f"{user[2]} failed to create account for {username}", user, 'fail', 'error')
        return False
 except sqlite3.Error as e:
            print(f"Error with create: {e}")
            return False

def check_user(username):
 try:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    conn.close()
    for user in users:
        if(decrypt_message(user[2]) == username):
            return True
    return False
 except sqlite3.Error as e:
            print(f"Error with fetch: {e}")
            return False

 except sqlite3.Error as e:
            print(f"Error with fetch: {e}")
            return False
def get_user(user_id):
 try:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users  WHERE ID = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return user
    else:
        return
 except sqlite3.Error as e:
            print(f"Error with fetch: {e}")
            return False

def get_users(user):
 try:
   conn = sqlite3.connect(db_path)
   conn.execute("PRAGMA foreign_keys = ON") 
   cursor = conn.cursor()

   cursor.execute('''
        SELECT Users.ID, Users.Rank, Users.Username, Profiles.Firstname, Profiles.Lastname
        FROM Users
        JOIN Profiles ON Users.ID = Profiles.UserID
    ''')

   rows = cursor.fetchall()
   conn.close()

   gebruikers_lijst = []
   for row in rows:
        decrypted = Userdetailsdecrypt(row)
        gebruiker_str = f"ID: {decrypted[0]} | Rank: {decrypted[1]} | Username: {decrypted[2]} | Firstname: {decrypted[3]} | Lastname: {decrypted[4]}"
        gebruikers_lijst.append(gebruiker_str)
 except sqlite3.Error as e:
        print("Error at:", e)
        return False
 return gebruikers_lijst
def updateprofilfirstnamee(id ,firstname, user):
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = ON") 
        cursor = conn.cursor()
        firstname = profilename_encrypt(firstname)
        cursor.execute('''
            UPDATE Profiles
            SET Firstname = ?
            WHERE UserID = ?
        ''', (firstname, id))

        conn.commit()
        conn.close()
        print("Profile succesfully edited.")
        log_actie(f"{user[2]} successfully updated profile  of user id {id}", user, 'success', 'normal')
      
    except sqlite3.Error as e:
        print("Error while editing:", e)
        log_actie(f"{user[2]} failed to update profile of user id {id}", user, 'fail', 'error')

def updateprofilelastname(id, lastname, user):
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = ON") 
        cursor = conn.cursor()
        lastname = profilename_encrypt(lastname)
        cursor.execute('''
            UPDATE Profiles
            Lastname = ? 
            WHERE UserID = ?
        ''',(lastname, id))

        conn.commit()
        conn.close()
        print("Profile succesfully edited.")
        log_actie(f"Systeem admin {user[2]} successfully updated their own profile", user, 'success', 'normal')
      
    except sqlite3.Error as e:
        print("Error while editing:", e)
        log_actie(f"Systeem admin {user[2]} failed to update their own profile", user, 'fail', 'error')
def getuserbyname(username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    conn.close()

    found = None

    for user in users:
        if(decrypt_message(user[2]) == username):
            user_list = list(user)            
            user_list[2] = decrypt_message(user[2])  
            found = user_list
            break
    return found
# Systeem admin

def CreateServiceMedewerker(username, password, firstname, lastname, user):
  check = add_user(username, password, 2, user)
  try:
   if check:
       engineer = getuserbyname(username)
       if user:
            add_profile_for_user(engineer[0], firstname, lastname, user)
            log_actie(f"Systeem admin {user[2]} successfully created profile for {engineer[2]}", user, 'success', 'normal')
       else:
           print("Error creating profile, could not find user")
           log_actie(f"Systeem admin {user[2]} failed created profile for {engineer[2]}", user, 'success', 'normal')
   
  except sqlite3.Error as e:
        print("Error at:", e)
        log_actie(f"Systeem admin {user[2]} failed created profile for {engineer[2]}", user, 'success', 'normal')
   
        return False
  return

def updateServiceEngineername(Engineer, username, user):
    username = Usersname_encrypt(username)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE Users
            SET Username = ?
            WHERE ID = ?
        ''', (username, Engineer[0]))

        conn.commit()
        print("User succesfully edited.")
        log_actie(f"Systeem admin {user[2]} successfully updated {Engineer[2]}", user, 'success', 'normal')
    except sqlite3.Error as e:
        print("Error while editing:", e)
        log_actie(f"Systeem admin {user[2]} failed to update {Engineer[2]}", user, 'fail', 'error')
    finally:
        conn.close()

def Deleteaccountown(user):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()
    try:


        cursor.execute("DELETE FROM Users WHERE ID = ?", (user[0],))

        conn.commit()
        conn.close()

        print(f"User successfully deleted returning to login.")
        log_actie(f"Systeem admin {user[2]} deleted self", user, 'success', 'normal')
        return True

    except sqlite3.Error as e:
        print("Error at:", e)
        log_actie(f"Systeem admin {user[2]} failed to delete self", user, 'fail', 'error')
        return False

def Deleteaccount(engineer, user):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()
    try:

        cursor.execute("DELETE FROM Users WHERE ID = ?", (engineer[0],))

        conn.commit()
        conn.close()

        print(f"User successfully deleted.")
        log_actie(f"Systeem admin {user[2]} deleted {engineer[2]}", user, 'success', 'normal')
        return True

    except sqlite3.Error as e:
        log_actie(f"Systeem admin {user[2]} failed to delete {engineer[2]}", user, 'fail', 'error')
        print("Error at:", e)
        return False

def passwordchangeengineer(engineer, pw, user ):
    try:
        hashed_pw = Hasher.hash_password(pw)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE Users SET Password = ? WHERE ID = ?", (hashed_pw, engineer[0]))
        conn.commit()                 
        conn.close()  
        print("Password updated.")
        log_actie(f"Systeem admin {user[2]} changed password of {engineer[2]}", user, 'success', 'normal')
    except sqlite3.Error as e:
        log_actie(f"Systeem admin {user[2]} failed to changed password of {engineer[2]}", user, 'fail', 'error')
        print("Error at:", e)
        return False
    

# super admin 

def CreateSysteemAdmin(username, password, firstname, lastname, user):
 try:
   check = add_user(username, password, 1, user)
   if check:
       newuser = getuserbyname(username)
       if user:
            add_profile_for_user(newuser[0], firstname, lastname, user)
       else:
           print("Error creating profile, could not find user")
   return
 except sqlite3.Error as e:
        log_actie(f"Super admin  failed to create system admin {username[2]}", user, 'fail', 'error')
        print("Error at:", e)
        return False

def updateSystemAdminname(admin, username, user):
    username = Usersname_encrypt(username)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE Users
            SET Username = ?
            WHERE ID = ?
        ''', (username, admin[0]))

        conn.commit()
        print("User succesfully edited.")
        log_actie(f"Super admin {user[2]} successfully updated {admin[2]}", user, 'success', 'normal')
    except sqlite3.Error as e:
        print("Error while editing:", e)
        log_actie(f"Super admin {user[2]} failed to update {admin[2]}", user, 'fail', 'error')
    finally:
        conn.close()

def Createbackupkey(user_id, backup_name, key_value):

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()
    key_value = key_encrypt(key_value)
    backup_name = key_encrypt(backup_name)
    try:
        cursor.execute('''
            INSERT INTO Backupkeys (Key, UserID, Backupname)
            VALUES (?, ?, ?)
        ''', (key_value, user_id, backup_name))
        conn.commit()
        conn.close()
        backup_name = decrypt_message(backup_name)
        sqlite_safe_backup(db_path, "Backups", backup_name)
        print("Backup key inserted successfully.")
    except Exception as e:
        print("Error inserting backup key:", e)

def restorebackup(user_id, keyvalue,  backup_dir="Backups"):
    
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON") 
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT ID, Key, UserID, Backupname FROM Backupkeys
        ''')
        results = cursor.fetchall()
        conn.close()
        for result in results:
            if(decrypt_message(result[1]) == keyvalue and result[2] == user_id): #  and result[2] == user_id
               backup = list(result)   
               backup[1] = decrypt_message(backup[1])# converteer naar lijst
               backup[3] = decrypt_message(backup[3])
               try:
                script_dir = os.path.dirname(os.path.abspath(__file__))
                full_backup_path = os.path.join(script_dir, backup_dir, backup[3])
                source = sqlite3.connect(full_backup_path)

                destination = sqlite3.connect(db_path)

                # Kopieer inhoud van source naar destination
                with destination:
                    copy_file(full_backup_path, db_path)
        
                    print("Back-up complete.")
    
               except Exception as e:
                    print(f"error with backup back-up: {e}")
    
               finally:
                source.close()
                destination.close()
                break
            else:
                print("Wrong key or user not found in keylist")




    except Exception as e:
        print("Error fetching all backup keys:")
        return 
def copy_file(source_path, destination_path):
    with open(source_path, 'rb') as src_file:
        with open(destination_path, 'wb') as dst_file:
            dst_file.write(src_file.read())
def sqlite_safe_backup(source_path, backup_folder, name):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = os.path.join(backup_folder, f"{name}.db")

    src_conn = sqlite3.connect(source_path)
    dest_conn = sqlite3.connect(backup_file)

    with dest_conn:
        src_conn.backup(dest_conn)

    src_conn.close()
    dest_conn.close()
    print(f"Veilige back-up gemaakt naar: {backup_file}")