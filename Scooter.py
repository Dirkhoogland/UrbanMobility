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
    print("What is the Serialnumber of the scooter, press  q to return.")
    Serialnumber = Validator.sanitize_input("Serialnumber: ")
    if Serialnumber == "q":
       return
    else:
        Scooter = Databasefunctions.GetScooterService(Serialnumber)
 
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
 
    print("What you can change is 1. State of Charge, 2. Target range SoC, 3. Location, 4. Out of Service status, 5. Milage, 6. last service date. leave empty if you dont wish to edit.")
 
    scooter = list(Scooter)  # converteer tuple naar lijst voor aanpassing
 
    # Invoer vragen (Enter = ongewijzigd)
    print("Leave empty to keep current value:")
    scooter_data = {}

    serialcheck = Speedcheck = batterycheck = soccheck = checktrs = servicecheck = maincheck = False

    scooter_data['Brand'] = Validator.sanitize_input("Scooter Brand: ")
    if scooter_data['Brand'] == "":
       scooter_data['Brand'] = Scooter[1]

    scooter_data['Model'] = Validator.sanitize_input("Scooter Model: ")
    if scooter_data['Model'] == "":
       scooter_data['Model'] = Scooter[2]

    while not serialcheck:
        scooter_data['SerialNumber'] = Validator.sanitize_input("Scooter Serial Number: ")
        if scooter_data ['SerialNumber'] != "":
            serialcheck = Validator.is_valid_serialnumber(scooter_data['SerialNumber'])
        else:
            scooter_data['SerialNumber'] = Scooter[3]

    while not Speedcheck:
        scooter_data['TopSpeed'] = input("Top Speed: ")
        if scooter_data ['TopSpeed'] != "":
            Speedcheck = Validator.is_valid_top_speed(scooter_data['TopSpeed'])
        else:
            scooter_data['SerialNumber'] = Scooter[4]

    while not batterycheck:
        scooter_data['BatteryCapacity'] = input("Battery Capacity: ")
        if scooter_data ['BatteryCapacity'] != "":
            batterycheck = Validator.is_valid_battery_capacity(scooter_data['BatteryCapacity'])
        else:
            scooter_data['BatteryCapacity'] = Scooter[5]

    while not soccheck:
        scooter_data['Soc'] = Validator.sanitize_input("State of Charge: ")
        if scooter_data ['Soc'] != "":
            soccheck = Validator.is_valid_soc(scooter_data['Soc'])
        else:
            scooter_data['Soc'] = Scooter[6]

    while not checktrs:
        scooter_data['TargetRange'] = Validator.sanitize_input("Target range SoC: ")
        if scooter_data ['TargetRange'] != "":
            checktrs = Validator.is_valid_soc(scooter_data['TargetRange'])
        else:
            scooter_data['TargetRange'] = Scooter[7]

    while not servicecheck:
        scooter_data['OutOfService'] = Validator.sanitize_input("Out of Service (0 of 1): ")
        if scooter_data ['OutOfService'] != "":
            servicecheck = Validator.validate_out_of_service(scooter_data['OutOfService'])
        else:
            scooter_data['OutOfService'] = Scooter[10]       

    scooter_data['Milage'] = Validator.sanitize_input("Mileage: ")
    if scooter_data ['Milage'] == "":
            scooter_data['Milage'] = Scooter[11]  
            
    while not maincheck:
        scooter_data['LastMaintenance'] = Validator.sanitize_input("Last Service Date (YYYY-MM-DD): ")
        if scooter_data ['LastMaintenance'] == "":
            maincheck = Validator.is_valid_maintenance_date(scooter_data['LastMaintenance'])
        else:
            scooter_data['LastMaintenance'] = Scooter[11]  
 

 

    Scooter[1] = scooter_data['Brand']
    Scooter[2] = scooter_data['Model']
    Scooter[3] = scooter_data['SerialNumber']
    Scooter[4] = scooter_data['TopSpeed']
    Scooter[5] = scooter_data['BatteryCapacity']
    Scooter[6] = scooter_data['Soc']
    Scooter[7] = scooter_data['TargetRange']
    Scooter[10] = scooter_data['OutOfService']
    Scooter[11] = scooter_data['Milage']
    Scooter[12] = scooter_data['LastMaintenance']
 
    check = Validator.sanitize_input("Wil je deze updaten? Y/N").upper()
    Scooter = scooter
    if check == "Y":
        Databasefunctions.ScooterupdateAdmin(Scooter, user)
    else:
        print("Update afgelast")
        sleep(100)
        return

def UpdateScooter(user):
    print("What is the Serialnumber of the scooter, press  q to return")
    Serialnumber = Validator.sanitize_input("Serialnumber: ")
    if Serialnumber == "q":
       return
    else:
        Scooter = Databasefunctions.GetScooterService(Serialnumber)
 
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
 
    scooter = list(Scooter)  # converteer tuple naar lijst voor aanpassing
    scooter_data = {}
    soccheck = checktrs = servicecheck = maincheck = False
    # Invoer vragen (Enter = ongewijzigd)
    print("leave empty to keep current value:")
    while not soccheck:
        scooter_data['Soc'] = Validator.sanitize_input("State of Charge: ")
        if scooter_data ['Soc'] != "":
            soccheck = Validator.is_valid_soc(scooter_data['Soc'])
        else:
            scooter_data['Soc'] = Scooter[6]

    while not checktrs:
        scooter_data['TargetRange'] = Validator.sanitize_input("Target range SoC: ")
        if scooter_data ['TargetRange'] != "":
            checktrs = Validator.is_valid_soc(scooter_data['TargetRange'])
        else:
            scooter_data['TargetRange'] = Scooter[7]

    while not servicecheck:
        scooter_data['OutOfService'] = Validator.sanitize_input("Out of Service (0 of 1): ")
        if scooter_data ['OutOfService'] != "":
            servicecheck = Validator.validate_out_of_service(scooter_data['OutOfService'])
        else:
            scooter_data['OutOfService'] = Scooter[10]       

    scooter_data['Milage'] = Validator.sanitize_input("Mileage: ")
    if scooter_data ['Milage'] == "":
            scooter_data['Milage'] = Scooter[11]  
            
    while not maincheck:
        scooter_data['LastMaintenance'] = Validator.sanitize_input("Last Service Date (YYYY-MM-DD): ")
        if scooter_data ['LastMaintenance'] == "":
            maincheck = Validator.is_valid_maintenance_date(scooter_data['LastMaintenance'])
        else:
            scooter_data['LastMaintenance'] = Scooter[11]  
    # Alleen wijzigen als input niet leeg is

    Scooter[6] = scooter_data['Soc']
    Scooter[7] = scooter_data['TargetRange']
    Scooter[10] = scooter_data['OutOfService']
    Scooter[11] = scooter_data['Milage']
    Scooter[12] = scooter_data['LastMaintenance']
 
    check = Validator.sanitize_input("Wil je deze updaten? Y/N").upper()
    Scooter = scooter
    if check == "Y":
        Databasefunctions.Scooterupdate(Scooter, user)
    else:
        print("Update afgelast")
        sleep(100)
        return
 
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
 
 