from curses import qiflush
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

def UpdateScooter(user):
    print("Wat is het Serialnumber van de scooter, vul in q om terug te gaan.")
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
 
    print("Wat je kan aan passen is 1. Top speed, 2. Battery Capacity, 3. State of Charge, 4. Target range SoC, 5. Location, 6. Out of Service status, 7. Milage, 8. last service date. laat het veld leeg als je deze niet wil aanpassen.")
 
    scooter = list(Scooter)  # converteer tuple naar lijst voor aanpassing
 
    # Invoer vragen (Enter = ongewijzigd)
    print("Laat leeg om huidige waarde te behouden:")
    speed = Validator.sanitize_input(f"Nieuwe Top Speed (huidig: {scooter[4]}")
 
    capacity = Validator.sanitize_input(f"Nieuwe Battery Capacity (huidig: {scooter[5]}): ")
 
    charge = Validator.sanitize_input(f"Nieuwe State of Charge (huidig: {scooter[6]}): ")
 
    Trs = Validator.sanitize_input(f"Nieuwe Target range SoC (huidig: {scooter[7]}): ")
 
    outofservice = Validator.sanitize_input(f"Out of Service (0 of 1) (huidig: {scooter[10]}): ")
 
    milage = Validator.sanitize_input(f"Nieuwe Mileage (huidig: {scooter[11]}): ")
 
    lastmain = Validator.sanitize_input(f"Last Service Date (YYYY-MM-DD) (huidig: {scooter[12]}): ")
 
    # Alleen wijzigen als input niet leeg is
    if speed:
        scooter[4] = speed
    if capacity:
        scooter[5] = capacity
    if charge:
        scooter[6] = charge
    if Trs:
        scooter[7] = Trs
    if outofservice:
        scooter[10] = int(outofservice)
    if milage:
        scooter[11] = int(milage)
    if lastmain:
        scooter[12] = lastmain
 
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
 
 