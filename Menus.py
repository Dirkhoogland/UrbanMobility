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
    return ["Add/modify Service Engineer", "Check Users", "Update Scooter","Get Scooter attributes", "Update Password", "Update Profile","Delete account", "Logout"]

def super():
    return ["Add/modify Service Engineer", "Check Users", "Update Scooter","Get Scooter attributes", "Update Password", "Logout"]

def addmodifyengineermenu():
    return ["Add new Service Engineer", "Modifty Service Engineer", "Remove Service Engineer", "Reset Service Engineer Password",]




