import Databasefunctions

def toon_dynamisch_menu(opties, titel="Hoofdmenu"):
    langste_optie = max([len(f"{i+1}. {optie}") for i, optie in enumerate(opties)])
    breedte = max(len(titel), langste_optie) + 4  # 4 extra voor ruimte

    print("╔" + "═" * breedte + "╗")
    print("║" + f" {titel} ".center(breedte) + "║")
    print("╠" + "═" * breedte + "╣")

    for i, optie in enumerate(opties, start=1):
        regel = f"{i}. {optie}"
        print("║ " + regel.ljust(breedte - 1) + "║")

    print("╚" + "═" * breedte + "╝")

def service():
    return ["1. Update Scooter","2. Get Scooter attributes", "3. Update Password", "4. Logout"]

def system():
    return ["1. Add/modify Service Engineer","2. Add/modify travellers", "3. Check Users", "4. Scooter info/update", "5. Update Password", "6. Update Profile","7. Delete account","8. Back up system","9. Restore back up","10. View logs", "11. Logout"]

def super():
    return ["Add/modify Service Engineer", "Check Users", "Update Scooter","Get Scooter attributes", "Update Password", "Logout"]

def addmodifyengineermenu():
    return ["Add new Service Engineer", "Modifty Service Engineer", "Remove Service Engineer", "Reset Service Engineer Password",]

def addmodifytravellers():
    return ["1. Add new Traveller", "2. Update Traveller in system", "3. Delete a traveller", "4. Search Traveller"]

def scooterinfo(rank):
    if rank == 2:
        return ["1. Update Scooter", "2. Get Scooter attributes"]
    if rank <= 1:
        return ["1. Update Scooter", "2. Get Scooter attributes", "3. Add new Scooter", "4. Delete Scooter", "5. Update information Scooter"]


def scooterattributes():

    scooters = Databasefunctions.FetchallScooter()
    opties = []

    for index, scooter in enumerate(scooters, start=1):
        # Maak een korte samenvatting, zoals merk en model
        optie = f"Merk: {scooter[1]} Model: {scooter[2]} Serialnumber: {scooter[3]} Top speed: {scooter[4]} BatteryCapacity: {scooter[5]} Soc: {scooter[6]} Target range: {scooter[7]} coords: {scooter[8]} {scooter[9]} Outofservice: {scooter[10]} Milage: {scooter[11]} Lastmaint: {scooter[12]}" 
        opties.append(optie)

    return opties

    


    