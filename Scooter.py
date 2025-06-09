from time import sleep
import Databasefunctions
import Menus , Validator

def UpdateScooter(user):
    print("Wat is het Serialnumber van de scooter, vul in q om terug te gaan.")
    Serialnumber = input("Serialnumber: ")
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
    speed = input(f"Nieuwe Top Speed (huidig: {scooter[4]}): ").strip()
    speed = Validator.sanitize_input(speed)

    capacity = input(f"Nieuwe Battery Capacity (huidig: {scooter[5]}): ").strip()
    capacity = Validator.sanitize_input(capacity)

    charge = input(f"Nieuwe State of Charge (huidig: {scooter[6]}): ").strip()
    charge = Validator.sanitize_input(charge)

    Trs = input(f"Nieuwe Target range SoC (huidig: {scooter[7]}): ").strip()
    Trs = Validator.sanitize_input(Trs)

    outofservice = input(f"Out of Service (0 of 1) (huidig: {scooter[10]}): ").strip()
    outofservice = Validator.sanitize_input(outofservice)

    milage = input(f"Nieuwe Mileage (huidig: {scooter[11]}): ").strip()
    milage = Validator.sanitize_input(milage)

    lastmain = input(f"Last Service Date (YYYY-MM-DD) (huidig: {scooter[12]}): ").strip()
    lastmain = Validator.sanitize_input(lastmain)

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

    check = input("Wil je deze updaten? Y/N")
    check.upper();
    check = Validator.sanitize_input(check)
    Scooter = scooter
    if check == "Y":
        Databasefunctions.Scooterupdate(Scooter)
    else:
        print("Update afgelast")
        sleep(100)
        return

def Getattributes(user):
    opties = Menus.scooterattributes()

    Menus.toon_dynamisch_menu(opties, "Scooter attributes")
    input( "test")


