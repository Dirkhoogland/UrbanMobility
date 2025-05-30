from time import sleep
import Databasefunctions


def UpdateScooter(user):
    Serialnumber = input("Wat is het Serialnumber van de scooter, vul in q om terug te gaan.")
    if Serialnumber == q:
       return
    else:
        Scooter = Databasefunctions.GetScooterService(Serialnumber)

    print(f"Scooter Brand: {Scooter[0]}")
    
    print(f"Scooter Model: {Scooter[1]}")
    
    print(f"Scooter Serial Number: {Scooter[2]}")
    
    print(f"Scooter Top speed: {Scooter[3]}")
    
    print(f"Scooter Battery Capacity: {Scooter[4]}")
    
    print(f"Scooter State of Charge: {Scooter[5]}")
    
    print(f"Scooter Target range SoC: {Scooter[6]}")

    print(f"Scooter Location: {Scooter[7]}")
    
    print(f"Scooter Out of Service status: {Scooter[8]}")

    print(f"Scooter Milage: {Scooter[9]}")
    
    print(f"Scooter Last service date: {Scooter[10]}")

    print("Wat je kan aan passen is 1. Top speed, 2. Battery Capacity, 3. State of Charge, 4. Target range SoC, 5. Location, 6. Out of Service status, 7. Milage, 8. last service date. laat het veld leeg als je deze niet wil aanpassen.")

    speed = input("Nieuwe Top speed: ")
    capacity = input("Nieuwe Battery Capacity: ")
    charge = input("Nieuwe State of Charge: ")
    Trs = input("Nieuwe Target range SoC: ")
    location = input("Nieuwe Location: ")
    outofservice = input("out of service: ")
    milage = input("Nieuwe Milage: ")
    lastmain = input("Last service date: ")

    if speed != " ":
        Scooter[3] = speed
    if capacity != " ":
        Scooter[4] = capacity
    if charge != " ":
        Scooter[5] = charge
    if Trs != " ":
        Scooter[6] = Trs
    if location != " ":
        Scooter[7] = location
    if outofservice != " ":
        Scooter[8] = outofservice
    if milage != " ":
        Scooter[9] = milage
    if lastmain != " ":
        Scooter[10] = lastmain

    print("Dit zijn de nieuwe gegevens van de scooter")
    print(f"Scooter Brand: {Scooter[0]}")
    
    print(f"Scooter Model: {Scooter[1]}")
    
    print(f"Scooter Serial Number: {Scooter[2]}")
    
    print(f"Scooter Top speed: {Scooter[3]}")
    
    print(f"Scooter Battery Capacity: {Scooter[4]}")
    
    print(f"Scooter State of Charge: {Scooter[5]}")
    
    print(f"Scooter Target range SoC: {Scooter[6]}")

    print(f"Scooter Location: {Scooter[7]}")
    
    print(f"Scooter Out of Service status: {Scooter[8]}")

    print(f"Scooter Milage: {Scooter[9]}")
    
    print(f"Scooter Last service date: {Scooter[10]}")
    check = input("Wil je deze updaten? Y/N")

    if check == "Y":
        Databasefunctions.Scooterupdate(Scooter)
    else:
        print("Update afgelast")
        sleep(100)
        return


