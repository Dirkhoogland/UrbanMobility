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
    return ["Update Scooter","Get Scooter attributes", "Update Password", "Logout"]

def system():
    return ["Add/modify Service Engineer","Add/modify travellers", "Check Users", "Scooter info/update", "Update Password", "Update Profile","Delete account","Back up system","Restore back up","View logs", "Logout"]

def super():
    return ["Add/modify Service Engineer", "Check Users", "Update Scooter","Get Scooter attributes", "Update Password", "Logout"]

def addmodifyengineermenu():
    return ["Add new Service Engineer", "Modifty Service Engineer", "Remove Service Engineer", "Reset Service Engineer Password",]

def addmodifytravellers():
    return ["Add new Traveller", "Update Traveller in system", "Delete a traveller", "Search Traveller"]

def scooterinfo(rank):
    if rank == 2:
        return ["1. Update Scooter", "2. Get Scooter attributes"]
    if rank <= 1:
        return ["1. Update Scooter", "2. Get Scooter attributes", "3. Add new Scooter", "4. Delete Scooter", "5. Update information Scooter"]


