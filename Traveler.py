import sqlite3
import os
import Hasher
import Validator 
import datetime
from Validator import is_valid_email, is_valid_phone, is_valid_DLN
from Menus import toon_dynamisch_menu, TravelerUpdateOptions, genderOption

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

def BirthdayManager():
    while True:
        try:
            Newbirthday = str(input("New Birthday (yyyy-mm-dd): ")).strip()
            frag = Newbirthday.split('-')

            if len(frag) != 3:
                print("Wrong format used, use the following format: (2025-01-01)")
                continue
            
            # year = int(frag[0]) 
            # month = int(frag[1])
            # day = int(frag[2])

            # 1 => 01 (month)
            if len(frag[1]) == 1: 
                frag[1] = "0" + frag[1]

            # 1 => 01 (day)
            if len(frag[2]) == 1: 
                frag[2] = "0" + frag[2]

            Newbirthday = frag[0] + "-" + frag[1] + "-" + frag[2]
            
            parsed_date = datetime.datetime.strptime(Newbirthday, "%Y-%m-%d").date() # used to check if date is valid

            return Newbirthday
        
        except:
            print("wrong format used, use fellowing format: (2025-01-01)")

def GenderManager():
    while True:
        try:
            choice = int(input("select option: "))
        except ValueError:
            print("invalid input, choose between number: ")
            continue

        if choice == 1:
            gender = "F"
            break
        
        if choice == 2:
            gender = "M"
            break

        print("invalid input, choose between number: ")
        print("[1] ♀ Female")
        print("[2] ♂ Male")
        continue

    return gender

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

        housenumber = ""
        while housenumber == "":
            housenumber = str(input("Housenumber: ")).strip()

        if(housenumber == "*"):
            quit = True
            break
        
        while housenumber < 0:
            try:
                housenumber = int(input("Streetnumber: "))
            except ValueError:
                print("Only numbers allowed")
                continue
            if(housenumber < 0): 
                print("No negative housenumbers allowed")

        city = ""
        while city == "":
            city = str(input("City: ")).strip()

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
        while is_valid_phone(phone) == False:
            phone = str(input("Phone: ")).strip()
            if(phone == "*"):
                quit = True
                break
            if is_valid_phone(phone) == False:
                print("phonenumber must have the lenght of 7 - 15")
                print("Example:")
                print("0612345678")

        if(phone == "*"):
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
        
    if quit == False:
        Add(firstname, lastname, birthday, gender, streetname, housenumber, city, email, phonenumber, DLN)
 

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
            toon_dynamisch_menu(genderOption(), "Select Gender")
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
            Newcity = ""
            while Newcity == "":
                Newcity = str(input("New City: ")).strip()
            cursor.execute('''
                UPDATE traveller SET City = ? WHERE EmailAdress = ?
            ''', (Newcity, Email))

            conn.commit()
            print("Update on Streetname succesfull")

        if option == 8:
            # phonenumber

            pass
            
        if option == 9:
            # drivings licence

            pass
        
        if option == 10:
            conn.close()
            break
    