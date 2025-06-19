import sqlite3
import os
from Databasefunctions import log_actie
from Validator import is_valid_email, is_valid_phone, is_valid_DLN, is_valid_zipCode, sanitize_input
from Menus import toon_dynamisch_menu, TravelerUpdateOptions, genderOption, cityOption
from Manager import BirthdayManager, GenderManager, cityManager
from DatabaseSetup import CreateBackup
from Encrypt import Traveller_encrypt,  encrypt_message
from Decrypt import Traveller_decrypt, decrypt_message
from logger import Log_encrypt

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.db")

def View(Email, User = "UNKNOWN"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Traveller
    ''')
    travellers = cursor.fetchall() 
    conn.close()

    for target in travellers:
        # traveller[1] = decrypt_message(traveller[1]) # Firstname
        # traveller[2] = decrypt_message(traveller[2]) # Lastname
        # traveller[5] = decrypt_message(traveller[5]) # Streetname
        # traveller[7] = decrypt_message(traveller[7]) # Zipcode
        # traveller[9] = decrypt_message(traveller[9]) # Email
        # traveller[10] = decrypt_message(traveller[10]) # phonenumber
        # traveller[11] = decrypt_message(traveller[11]) # DLN
        # Email is encrypted
        if(decrypt_message(target[9]) == Email):
            # Log_encrypt()
            return Traveller_decrypt(target)
    return None
    
def abortAdd(string):
    return string == "*"

def AddTraveller(user):

    print("press * and enter at any point abort adding process")
    quit = False
    while True:
        firstname = ""
        while firstname == "":
            firstname = str(sanitize_input("Firstname: ")).capitalize().strip()
        
        if(firstname == "*"):
            quit = True
            break

        lastname = ""
        while lastname == "":
            lastname = str(sanitize_input("Lastname: ")).capitalize().strip()

        if(lastname == "*"):
            quit = True
            break

        birthday = BirthdayManager()
        
        if(birthday == "*"):
            quit = True
            break

        gender = GenderManager()

        if(gender == "*"):
            quit = True
            break

        streetname = ""
        while streetname == "":
            streetname = str(sanitize_input("Streetname: ")).strip()

        if(streetname == "*"):
            quit = True
            break
        
        housenumber = -1
        while housenumber < 0:
            try:
                housenumber = int(sanitize_input("Streetnumber: "))
            except ValueError:
                print("Only numbers allowed")
                continue
            if(housenumber < 0): 
                print("No negative housenumbers allowed")

        city = cityManager()

        if(city == "*"):
            quit = True
            break

        zipCode = "-1"  # place holder
        while is_valid_zipCode(zipCode) == False:
            zipCode = str(sanitize_input("Zipcode: ")).upper().strip()
            if(zipCode == "*"):
                quit = True
                break
            if is_valid_zipCode(zipCode) == False:
                print("Zipcode must start with 2 letters and end with 4 numbers")
                print("Example:")
                print("1234AB")

        if(zipCode == "*"):
            quit = True
            break

        email = ""
        while True:
            email = str(sanitize_input("Email: ")).strip()
            if(email == "*"):
                quit = True
                break
            if is_valid_email(email) == False:
                print("Email must have the fellowing pattern")
                print("Example:")
                print("example@gmail.com")
                continue
            if View(email) != None:
                print(f"A user with email of '{email}' already exists,\nyou can update existing user data by ussing the update menu if it requires changes")
                email = ""
                continue
            break


        if(email == "*"):
            quit = True
            break

        phonenumber = ""
        while is_valid_phone(phonenumber) == False:
            phonenumber = "31-6-" + str(input("PhoneNumber in format +31-6-DDDDDDDD: +31-6-")).strip()
            if(phonenumber == "31-6-*"):
                quit = True
                break
            if is_valid_phone(phonenumber) == False:
                print("phonenumber must have the lenght of 8")
                print("Example:")
                print("31-6-12345678")

        if(phonenumber == "*"):
            quit = True
            break

        phonenumber = "+" + phonenumber

        DLN = ""
        while is_valid_DLN(DLN) == False:
            DLN = str(sanitize_input("DrivingsLicenceNumber in [AB1234567] or [A12345678] format: ")).upper().strip()
            if(DLN == "*"):
                quit = True
                break
            if is_valid_DLN(DLN) == False:
                print("send an invalid DrivingsLicenceNumber format, use a valid format")
                print("Example:")
                print("AB1234567")
                print("A12345678")

        if(DLN == "*"):
            quit = True
            break

        break
        
    if quit == False:
        Add(firstname, lastname, birthday, gender, streetname, housenumber, zipCode, city, email, phonenumber, DLN, user)
    else:
        print("aborted adding traveller process")
 

def Add(Firstname, Lastname, Birthday, Gender, Streetname, 
        Housenumber, zipCode, City, EmailAdress, MobilePhone, DrivingLiscenceNumber, user):
    try:
        traveller = (Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, zipCode, City, EmailAdress, MobilePhone, DrivingLiscenceNumber)
        traveller = Traveller_encrypt(traveller) # encrypt privacy intensive fields
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO Traveller (
            Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, 
            zipCode, City, EmailAdress, MobilePhone, DrivingLiscenceNumber
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', traveller)

        conn.commit()
        print("New traveller succesfully added")
        log_actie(f"{user[2]} successfully added a traveller ", user, 'sucess', 'normal')
    except sqlite3.OperationalError: 
        print("Failed to add Traveller")
        log_actie(f"{user[2]} Failed to add Traveller ", user, 'error', 'fail')
    finally:
        if conn:
            conn.close()


def Update(Email, user):
    conn = None # for finnaly block if sqlite3.connect(db_path) fails 
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        while True:
            Id = -1
            traveller = View(Email)
            if traveller == None:
                print("user not found")
                break
            print(traveller)
            Id = traveller[0]
            
            print()
            print("what do you want to update?")
            toon_dynamisch_menu(TravelerUpdateOptions(), "Traveller Update Menu")
            try:
                option = int(input("Select option: "))
            except ValueError:
                print("invalid input, choose a number.")
                continue
            if option == 1:
                Newfirstname = ""
                while Newfirstname == "":
                    Newfirstname = str(sanitize_input("New Firstname: ")).capitalize().strip()

                cursor.execute('''
                    UPDATE traveller SET Firstname = ? WHERE ID = ?
                ''', (encrypt_message(Newfirstname), Id,))
            
                conn.commit()
                print("Update on Firstname succesfull")
                log_actie(f"{user[2]} successfully updated a traveller ", user, 'sucess', 'normal')
            if option == 2:
                Newlastname = ""
                while Newlastname == "":
                    Newlastname = str(("New Lastname: ")).capitalize().strip()
                cursor.execute('''
                    UPDATE traveller SET Lastname = ? WHERE ID = ?
                ''', (encrypt_message(Newlastname), Id))

                conn.commit()
                print("Update on Lastname succesfull")
                log_actie(f"{user[2]} successfully updated a traveller ", user, 'sucess', 'normal')
            if option == 3:
                while True:
                    Newbirthday = BirthdayManager()

                    cursor.execute('''
                    UPDATE traveller SET Birthday = ? WHERE ID = ?
                    ''', (Newbirthday, Id))

                    conn.commit()
                    print("Update on Birthday succesfull")
                    break
                    
            if option == 4:
                # Gender update
                gender = GenderManager()

                if gender == "F" or gender == "M":

                    cursor.execute('''
                    UPDATE traveller SET Gender = ? WHERE ID = ?
                    ''', (gender, Id))

                    conn.commit()
                    print("Update on Gender succesfull")
                    log_actie(f"{user[2]} successfully updated a traveller ", user, 'sucess', 'normal')
            if option == 5:
                Newstreetname = ""
                while Newstreetname == "":
                    Newstreetname = str(sanitize_input("New Streetname: ")).strip()
                conn.execute('''
                    UPDATE traveller SET Streetname = ? WHERE ID = ?
                ''', (encrypt_message(Newstreetname), Id))

                conn.commit()
                print("Update on Streetname succesfull")

            if option == 6:
                Newhousenumber = -1
                while Newhousenumber < 0:
                    try:
                        Newhousenumber = int(input("New Streetnumber: "))
                    except ValueError:
                        print("Only numbers allowed")
                        continue
                    if(Newhousenumber < 0): 
                        print("No negative housenumbers allowed")

                cursor.execute('''
                    UPDATE traveller SET HouseNumber = ? WHERE ID = ?
                ''', (Newhousenumber, Id))

                conn.commit()
                print("Update on Housenumber succesfull")
                log_actie(f"{user[2]} successfully updated a traveller ", user, 'sucess', 'normal')
            if option == 7:
                NewzipCode = "-1"  # place holder
                while is_valid_zipCode(NewzipCode) == False:
                    NewzipCode = str(sanitize_input("Zipcode: ")).upper().strip()
                    if is_valid_zipCode(NewzipCode) == False:
                        print("Zipcode must start with 2 letters and end with 4 numbers")
                        print("Example:")
                        print("AB1234")

                cursor.execute('''
                    UPDATE traveller SET ZipCode = ? WHERE ID = ?
                ''', (encrypt_message(NewzipCode), Id))

                conn.commit()
                print("Update on Zipcode succesfull")

            if option == 8:
                Newcity = "UNKNOWN" # place holder
                Newcity = cityManager()
                cursor.execute('''
                    UPDATE traveller SET City = ? WHERE ID = ?
                ''', (Newcity, Id))

                conn.commit()
                print("Update on City succesfull")
                log_actie(f"{user[2]} successfully updated a traveller ", user, 'sucess', 'normal')                

            if option == 9:
                # phonenumber
                Newphonenumber = "-1" # place holder
                while is_valid_phone(Newphonenumber) == False:
                    Newphonenumber = "31-6-" + str(sanitize_input("PhoneNumber in format +31-6-DDDDDDDD: +31-6-")).strip()
                    if is_valid_phone(Newphonenumber) == False:
                        print("phonenumber must have the lenght of 8")
                        print("Example:")
                        print("+31-6-12345678")

                Newphonenumber = "+" + Newphonenumber 

                cursor.execute('''
                    UPDATE traveller SET MobilePhone = ? WHERE ID = ?
                ''', (encrypt_message(Newphonenumber), Id))
                
                conn.commit()
                print("Update on MobilePhone succesfull")
                log_actie(f"{user[2]} successfully updated a traveller ", user, 'sucess', 'normal')                
            if option == 10:
                DLN = "-1" # place holder
                while is_valid_DLN(DLN) == False:
                    DLN = str(sanitize_input("DrivingsLicenceNumber in [AB1234567] or [A12345678] format: ")).upper().strip()
                    if is_valid_DLN(DLN) == False:
                        print("send an invalid DrivingsLicenceNumber format, use a valid format")
                        print("Example:")
                        print("AB1234567")
                        print("A12345678")
                
                cursor.execute('''
                    UPDATE traveller SET DrivingLiscenceNumber = ? WHERE ID = ?
                ''', (encrypt_message(DLN), Id))

                conn.commit()
                print("Update on DrivingLiscenceNumber succesfull")
                log_actie(f"{user[2]} successfully updated a traveller ", user, 'sucess', 'normal')            
            if option == 11:
                break

    except sqlite3.OperationalError:
        print("An error accured rebooting...")
        log_actie(f"{user[2]} failed to update a traveller ", user, 'Error', 'fail')
        if conn:
            conn.close()

def Delete(Email, user):
    try:
        conn = None
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        Id = -1
        traveller = View(Email)
        if traveller == None:
            print("user not found")
            return
        print(traveller)
        Id = traveller[0]

        cursor.execute('''
        DELETE FROM Traveller
        WHERE ID = ?
        ''', (Id,))

        conn.commit()
        print("Traveller deleted successfully.")
        log_actie(f"{user[2]} succesfully deleted a traveller ", user, 'sucess', 'normal')
    except sqlite3.OperationalError:
        ("An error accured rebooting...")
        log_actie(f"{user[2]} failed to delete a traveller ", user, 'Error', 'fail')
    finally:
        if conn:
            conn.close()
