import sqlite3
import os
import Hasher
import Validator 
import datetime
from Validator import is_valid_email, is_valid_phone, is_valid_DLN
from Menus import toon_dynamisch_menu, TravelerUpdateOptions, genderOption, cityOption
from Manager import BirthdayManager, GenderManager, cityManager

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
    
    conn.close()

def abortAdd(string):
    return string == "*"

def AddTraveller():
    print("press * and enter at any point abort adding process")
    quit = False
    while True:
        firstname = ""
        while firstname == "":
            firstname = str(input("Firstname: ")).strip()
        
        if(firstname == "*"):
            quit = True
            break

        lastname = ""
        while lastname == "":
            lastname = str(input("Lastname: ")).strip()

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
            streetname = str(input("Streetname: ")).strip()

        if(streetname == "*"):
            quit = True
            break
        
        housenumber = -1
        while housenumber < 0:
            try:
                housenumber = int(input("Streetnumber: "))
            except ValueError:
                print("Only numbers allowed")
                continue
            if(housenumber < 0): 
                print("No negative housenumbers allowed")

        city = cityManager()

        if(city == "*"):
            quit = True
            break

        email = ""
        while is_valid_email(email) == False:
            email = str(input("Email: ")).strip()
            if(email == "*"):
                quit = True
                break
            if is_valid_email(email) == False:
                print("Email must have the fellowing pattern")
                print("Example:")
                print("example@gmail.com")

        if(email == "*"):
            quit = True
            break

        phonenumber = ""
        while is_valid_phone(phonenumber) == False:
            phonenumber = str(input("Phone: ")).strip()
            if(phonenumber == "*"):
                quit = True
                break
            if is_valid_phone(phonenumber) == False:
                print("phonenumber must have the lenght of 7 - 15")
                print("Example:")
                print("0612345678")

        if(phonenumber == "*"):
            quit = True
            break

        DLN = ""
        while is_valid_DLN(DLN) == False:
            DLN = str(input("DrivingsLicenceNumber: ")).upper().strip()
            if(DLN == "*"):
                quit = True
                break
            if is_valid_DLN(DLN) == False:
                print("DrivingsLicenceNumber must have the fellowing pattern: r'^[A-Z]{1}\d{8}$' or r'^[A-Z]{2}\d{7}$'")
                print("Example:")
                print("AB1234567")
                print("A12345678")

        if(DLN == "*"):
            quit = True
            break

        break
        
    if quit == False:
        Add(firstname, lastname, birthday, gender, streetname, housenumber, city, email, phonenumber, DLN)
    else:
        print("aborted adding traveller process")
 

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

    conn.commit()
    print("New travler succesfully added")
    conn.close()


def Update(Email):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    while True:
        View(Email)
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
                Newfirstname = str(input("New Firstname: ")).strip()

            cursor.execute('''
                UPDATE traveller SET Firstname = ? WHERE EmailAdress = ?
            ''', (Newfirstname, Email,))
           
            conn.commit()
            print("Update on Firstname succesfull")

        if option == 2:
            Newlastname = ""
            while Newlastname == "":
                Newlastname = str(input("New Lastname: ")).strip()
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
                Newstreetname = str(input("New Streetname: ")).strip()
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
            Newcity = "UNKNOWN" # place holder
            while Newcity == "":
                Newcity = cityManager()
            cursor.execute('''
                UPDATE traveller SET City = ? WHERE EmailAdress = ?
            ''', (Newcity, Email))

            conn.commit()
            print("Update on City succesfull")

        if option == 8:
            # phonenumber
            phonenumber = ""
            while is_valid_phone(phonenumber) == False:
                phonenumber = str(input("PhoneNumber: ")).strip()
                if is_valid_phone(phonenumber) == False:
                    print("phonenumber must have the lenght of 7 - 15")
                    print("Example:")
                    print("0612345678")

            cursor.execute('''
                UPDATE traveller SET MobilePhone = ? WHERE EmailAdress = ?
            ''', (phonenumber, Email))
            
            conn.commit()
            print("Update on MobilePhone succesfull")
            
        if option == 9:
            # drivings licence
            DLN = ""
            while is_valid_DLN(DLN) == False:
                DLN = str(input("DrivingsLicenceNumber: ")).upper().strip()
                if is_valid_DLN(DLN) == False:
                    print("DrivingsLicenceNumber must have the fellowing pattern: r'^[A-Z]{1}\d{8}$' or r'^[A-Z]{2}\d{7}$'")
                    print("Example:")
                    print("AB1234567")
                    print("A12345678")
            
            cursor.execute('''
                UPDATE traveller SET DrivingLiscenceNumber = ? WHERE EmailAdress = ?
            ''', (DLN, Email))

            conn.commit()
            print("Update on DrivingLiscenceNumber succesfull")
        
        if option == 10:
            conn.close()
            break
    