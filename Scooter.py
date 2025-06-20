from time import sleep
import Databasefunctions
import Menus , Validator
def newscooter(user):
    scooter_data = {}

    serialcheck = Speedcheck = batterycheck = soccheck = checktrs = servicecheck = maincheck = False

    scooter_data['Brand'] = Validator.sanitize_input("Scooter Brand: ")
    scooter_data['Model'] = Validator.sanitize_input("Scooter Model: ")

    while not serialcheck:
        scooter_data['SerialNumber'] = Validator.sanitize_input("Scooter Serial Number: ")
        serialcheck = Validator.is_valid_serialnumber(scooter_data['SerialNumber'])

    while not Speedcheck:
        scooter_data['TopSpeed'] = input("Top Speed: ")
        Speedcheck = Validator.is_valid_top_speed(scooter_data['TopSpeed'])

    while not batterycheck:
        scooter_data['BatteryCapacity'] = input("Battery Capacity: ")
        batterycheck = Validator.is_valid_battery_capacity(scooter_data['BatteryCapacity'])

    while not soccheck:
        scooter_data['Soc'] = Validator.sanitize_input("State of Charge: ")
        soccheck = Validator.is_valid_soc(scooter_data['Soc'])

    while not checktrs:
        scooter_data['TargetRange'] = Validator.sanitize_input("Target range SoC: ")
        checktrs = Validator.is_valid_soc(scooter_data['TargetRange'])

    while not servicecheck:
        scooter_data['OutOfService'] = input("Out of Service (0 of 1): ")
        servicecheck = Validator.validate_out_of_service(scooter_data['OutOfService'])

    scooter_data['Milage'] = Validator.sanitize_input("Mileage: ")

    while not maincheck:
        scooter_data['LastMaintenance'] = input("Last Service Date (YYYY-MM-DD): ")
        maincheck = Validator.is_valid_maintenance_date(scooter_data['LastMaintenance'])


def UpdateScooteradmin(user):
 
    print("What is the Serialnumber of the scooter, press  q to return")
    Serialnumber = Validator.sanitize_input("Serialnumber: ")
    if Serialnumber == "q":
       return
    else:
        Scooter = Databasefunctions.GetScooterService(Serialnumber)
        if not Scooter:
            print("SCooter could not be found")
            return
        
 
    print(f"Scooter Brand: {Scooter[1]}")
   
    print(f"Scooter Model: {Scooter[2]}")
   
    print(f"Scooter Serial Number: {Scooter[3]}")
   
    print(f"Scooter Top speed: {Scooter[4]}")
   
    print(f"Scooter Battery Capacity: {Scooter[5]}")
   
    print(f"Scooter State of Charge: {Scooter[6]}")
   
    print(f"Scooter Target range SoC: {Scooter[7]}")
 
    print(f"Scooter Location: {Scooter[8]}, {Scooter[9]}")
   
    print(f"Scooter Out of Service status: {Scooter[10]}")
 
    print(f"Scooter Milage: {Scooter[11]}")
   
    print(f"Scooter Last service date: {Scooter[12]}")
    menu = True
    while menu == True:
        Opties = Menus.scooteredit(user[1])
        Menus.toon_dynamisch_menu(Opties, "scooter edit")
        optie = Validator.int_input("Select option: ")
        if optie == 1:
            Brand(Scooter[3], user)
        if optie == 2:
            Model(Scooter[3], user)
        if optie == 3:
            serialnumber(Scooter[3], user)
            return
        if optie == 4:
            topspeed(Scooter[3], user)
        if optie == 5:
            Batterycapacity(Scooter[3], user)
        if optie == 6:
             StateOfCharge(Scooter[3], user)
        if optie == 7:
            targetrange(Scooter[3], user)
        if optie == 8:
            Location(Scooter[3], user)
        if optie == 9:
            OutOfService(Scooter[3], user)
        if optie == 10:
            Milage(Scooter[3], user)
        if optie == 11:
            Lastmaint(Scooter[3], user)
        if optie == 12:
            menu == False
            return

def UpdateScooter(user):
    print("What is the Serialnumber of the scooter, press  q to return")
    Serialnumber = Validator.sanitize_input("Serialnumber: ")
    if Serialnumber == "q":
       return
    else:
        Scooter = Databasefunctions.GetScooterService(Serialnumber)
        if not Scooter:
            print("SCooter could not be found")
            return
        
 
    print(f"Scooter Brand: {Scooter[1]}")
   
    print(f"Scooter Model: {Scooter[2]}")
   
    print(f"Scooter Serial Number: {Scooter[3]}")
   
    print(f"Scooter Top speed: {Scooter[4]}")
   
    print(f"Scooter Battery Capacity: {Scooter[5]}")
   
    print(f"Scooter State of Charge: {Scooter[6]}")
   
    print(f"Scooter Target range SoC: {Scooter[7]}")
 
    print(f"Scooter Location: {Scooter[8]}, {Scooter[9]}")
   
    print(f"Scooter Out of Service status: {Scooter[10]}")
 
    print(f"Scooter Milage: {Scooter[11]}")
   
    print(f"Scooter Last service date: {Scooter[12]}")
    menu = True
    while menu == True:
        Opties = Menus.scooteredit(user[1])
        Menus.toon_dynamisch_menu(Opties, "scooter edit")
        optie = Validator.int_input("Select option: ")
        if optie == 1:
             StateOfCharge(Scooter[3], user)
        if optie == 2:
            targetrange(Scooter[3], user)
        if optie == 3:
            Location(Scooter[3], user)
        if optie == 4:
            OutOfService(Scooter[3], user)
        if optie == 5:
            Milage(Scooter[3], user)
        if optie ==6:
            Lastmaint(Scooter[3], user)
        if optie == 7:
            menu == False
            return
def Batterycapacity(Serialnumber, user):
   
        mil = Validator.sanitize_input("Batterycapacity: ")

        soccheck =  Validator.is_valid_battery_capacity(mil)
        if soccheck == True:
           Databasefunctions.battery(mil, Serialnumber, user)
        else:
            print("Invalid data")
def Brand(Serialnumber, user):
        brand = Validator.sanitize_input("brand: ")
        Databasefunctions.brand(brand, Serialnumber, user)
def serialnumber(Serialnumber, user):
        ser = Validator.sanitize_input("Serialnumber: ")

        soccheck =  Validator.is_valid_serialnumber(ser)
        if soccheck == True:
           Databasefunctions.Serialnumber(ser, Serialnumber, user)
        else:
            print("Invalid data")
def Model(Serialnumber, user):
        brand = Validator.sanitize_input("Model: ")
        Databasefunctions.model(brand, Serialnumber, user)
def Lastmaint(Serialnumber, user):
   
        mil = Validator.sanitize_input("Last Service Date (YYYY-MM-DD): ")

        soccheck =  Validator.is_valid_maintenance_date(mil)
        if soccheck == True:
           Databasefunctions.maintdate(mil, Serialnumber, user)
        else:
            print("Invalid data")
def topspeed(Serialnumber, user):
   
        mil = Validator.sanitize_input("Top speed: ")

        soccheck =  Validator.is_valid_top_speed(mil)
        if soccheck == True:
           Databasefunctions.Speed(mil, Serialnumber, user)
        else:
            print("Invalid data")
def Milage(Serialnumber, user):
   
        mil = Validator.sanitize_input("Milage: ")

        soccheck =  Validator.is_valid_milage(mil)
        if soccheck == True:
           Databasefunctions.Milage(mil, Serialnumber, user)
        else:
            print("Invalid data")
def OutOfService(Serialnumber, user):
   
        soc = Validator.sanitize_input("Out of Service 0 or 1: ")

        soccheck =  Validator.validate_out_of_service(soc)
        if soccheck == True:
           Databasefunctions.OutOfService(soc, Serialnumber, user)
        else:
            print("Invalid data")
def StateOfCharge(Serialnumber, user):
        soc = Validator.sanitize_input("State of Charge: ")

        soccheck = Validator.is_valid_soc(soc)
        if soccheck == True:
           Databasefunctions.StateofChargeupdate(soc, Serialnumber, user)
        else:
            print("Invalid data")
def targetrange(Serialnumber, user):
        rnge = Validator.sanitize_input("target range: ")

        soccheck = Validator.is_valid_soc(rnge)
        if soccheck == True:
          Databasefunctions.targetrangeupdate(rnge, Serialnumber, user)
        else:
            print("Invalid data")
def Location(Serialnumber, user):
        lat = Validator.sanitize_input("Lat: ")
        long = Validator.sanitize_input("Long: ")
        soccheck = Validator.is_valid_latitude(lat)
        if soccheck == True:
            check = Validator.is_valid_longitude(long)
            if check == True:
                 Databasefunctions.LocationUpdate(lat, long, Serialnumber, user)
        else:
            print("Invalid data")
def Getattributes(user):
    opties = Menus.scooterattributes()
 
    Menus.toon_dynamisch_menu(opties, "Scooter attributes")
    input( "Press enter to continue . . .")

def Deletescooter(user):
    serialcheck = False
    while not serialcheck:
        number = Validator.sanitize_input("Scooter Serial Number: ")
        serialcheck = Validator.is_valid_serialnumber(number)
    Databasefunctions.DeleteScooter(number, user)
 
 