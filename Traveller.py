import sqlite3
import os
from Validator import is_valid_email, is_valid_phone, is_valid_DLN, is_valid_zipCode, sanitize_input
from Menus import toon_dynamisch_menu, TravelerUpdateOptions, genderOption, cityOption
from Manager import BirthdayManager, GenderManager, cityManager
from DatabaseSetup import CreateBackup

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.db")

def View(Email):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Traveller WHERE EmailAdress = ?
    ''', (Email,))
    target = cursor.fetchone()
    conn.close()
    
    return target
    
def abortAdd(string):
    return string == "*"

def AddTraveller():

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
        Add(firstname, lastname, birthday, gender, streetname, housenumber, zipCode, city, email, phonenumber, DLN)
    else:
        print("aborted adding traveller process")
 

def Add(Firstname, Lastname, Birthday, Gender, Streetname, 
        Housenumber, zipCode, City, EmailAdress, MobilePhone, DrivingLiscenceNumber):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        traveller = [
            (Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, zipCode, City, EmailAdress, MobilePhone, DrivingLiscenceNumber)
        ]
        cursor.executemany('''
        INSERT INTO Traveller (
            Firstname, Lastname, Birthday, Gender, Streetname, Housenumber, 
            zipCode, City, EmailAdress, MobilePhone, DrivingLiscenceNumber
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', traveller)

        conn.commit()
        print("New travler succesfully added")
    except sqlite3.OperationalError: 
        print("Failed to add Traveller")
    finally:
        if conn:
            conn.close()


def Update(Email):
    CreateBackup()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        while True:
        
            traveller = View(Email)
            if traveller == None:
                print("user not found")
                break

            print(traveller)
            
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
                    UPDATE traveller SET Firstname = ? WHERE EmailAdress = ?
                ''', (Newfirstname, Email,))
            
                conn.commit()
                print("Update on Firstname succesfull")

            if option == 2:
                Newlastname = ""
                while Newlastname == "":
                    Newlastname = str(("New Lastname: ")).capitalize().strip()
                cursor.execute('''
                    UPDATE traveller SET Lastname = ? WHERE EmailAdress = ?
                ''', (Newlastname, Email))

                conn.commit()
                print("Update on Lastname succesfull")

            if option == 3:
                while True:
                    Newbirthday = BirthdayManager()

                    cursor.execute('''
                    UPDATE traveller SET Birthday = ? WHERE EmailAdress = ?
                    ''', (Newbirthday, Email))

                    conn.commit()
                    print("Update on Birthday succesfull")
                    break
                    
            if option == 4:
                # Gender update
                gender = GenderManager()

                if gender == "F" or gender == "M":

                    cursor.execute('''
                    UPDATE traveller SET Gender = ? WHERE EmailAdress = ?
                    ''', (gender, Email))

                    conn.commit()
                    print("Update on Gender succesfull")

            if option == 5:
                Newstreetname = ""
                while Newstreetname == "":
                    Newstreetname = str(sanitize_input("New Streetname: ")).strip()
                conn.execute('''
                    UPDATE traveller SET Streetname = ? WHERE EmailAdress = ?
                ''', (Newstreetname, Email))

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
                    UPDATE traveller SET HouseNumber = ? WHERE EmailAdress = ?
                ''', (Newhousenumber, Email))

                conn.commit()
                print("Update on Housenumber succesfull")

            if option == 7:
                NewzipCode = "-1"  # place holder
                while is_valid_zipCode(NewzipCode) == False:
                    NewzipCode = str(sanitize_input("Zipcode: ")).upper().strip()
                    if is_valid_zipCode(NewzipCode) == False:
                        print("Zipcode must start with 2 letters and end with 4 numbers")
                        print("Example:")
                        print("AB1234")

                cursor.execute('''
                    UPDATE traveller SET ZipCode = ? WHERE EmailAdress = ?
                ''', (NewzipCode, Email))

                conn.commit()
                print("Update on Zipcode succesfull")

            if option == 8:
                Newcity = "UNKNOWN" # place holder
                Newcity = cityManager()
                cursor.execute('''
                    UPDATE traveller SET City = ? WHERE EmailAdress = ?
                ''', (Newcity, Email))

                conn.commit()
                print("Update on City succesfull")
                

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
                    UPDATE traveller SET MobilePhone = ? WHERE EmailAdress = ?
                ''', (Newphonenumber, Email))
                
                conn.commit()
                print("Update on MobilePhone succesfull")
                
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
                    UPDATE traveller SET DrivingLiscenceNumber = ? WHERE EmailAdress = ?
                ''', (DLN, Email))

                conn.commit()
                print("Update on DrivingLiscenceNumber succesfull")
            
            if option == 11:
                break

    except sqlite3.OperationalError:
        print("An error accured rebooting...")
    finally:
        if conn:
            conn.close()
