import Scooter, Gebruiker , Menus , Databasefunctions , Profiles, Servicemedewerker, Validator, SysAdmin
import Validator 

def ServiceEngineeredit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "super Admin edit engineer")
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
        if optie == 1:
            Gebruiker.Addservice(user)
        if optie == 2:
            Gebruiker.UpdateEngineer(user)
        if optie == 3:
            Gebruiker.Deleteother(user)
        if optie == 4:
            Gebruiker.changepasswordengineer(user)
        if optie == 5:
            Profiles.ViewProfile(user)
        else:
            menu = False
    return
def SysteemadminEdit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "super Admin edit System Admin")
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
        if optie == 1:
            Gebruiker.AddSysteemmedewerker(user)
        if optie == 2:
            Gebruiker.UpdateSysteemadmin(user)
        if optie == 3:
            Gebruiker.Deleteother(user)
        if optie == 4:
            Gebruiker.changepasswordengineer(user)
        if optie == 5:
            Profiles.ViewProfile(user)
        else:
            menu = False
    return

def SuperMenu(user):
    menu = True
    while menu == True:
        opties = Menus.super()
        Menus.toon_dynamisch_menu(opties, "Super Admin")
# def super():
#     return ["User list","Add/Modify System Admin", "Add/modify Service Engineer","Add/modify travellers", "Scooter info/update", "Profile", "Back up Code","Create back up", "View logs", "Logout"]
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue

        if optie == 1:
            Gebruiker.ViewUserlist(user)
        if optie == 2:
            SysteemadminEdit(user)
        if optie == 3:
            ServiceEngineeredit(user)
        if optie == 4:
            Gebruiker.changepasswordengineer(user)
        if optie == 5:
            Profiles.ViewProfile(user)
        else:
            menu = False
            SuperMenu(user)