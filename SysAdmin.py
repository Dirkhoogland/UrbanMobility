from email.policy import default
from pickle import FALSE
import Traveller
import Scooter, Gebruiker , Menus , Databasefunctions , Profiles, Servicemedewerker, Validator
import Validator 
import Superadmin

def ServiceEngineeredit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "Sys Admin edit engineer")

        optie = Validator.int_input("Select option: ")
        if optie == 1:
            Gebruiker.Addservice(user)
        if optie == 2:
            Gebruiker.UpdateEngineer(user)
        if optie == 3:
            Gebruiker.Deleteother(user)
        if optie == 4:
            Gebruiker.changepasswordengineer(user)
        else:
            menu = False
            SysMenu(user)


def TravellerMenu(user):
    Traveller.TravellerMenu(user)

def scootermenu(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.TravelerUpdateOptions(user[1])
        Menus.toon_dynamisch_menu(optiesmenu, "Systeem Admin edit Traveller ")
        optie = Validator.int_input("Select option: ")
        if optie == 1:
            Scooter.UpdateScooteradmin(user)
        if optie == 2:
            Scooter.Getattributes(user)
        if optie == 3:
            Scooter.newscooter(user)
        if optie == 4:
            Scooter.Deletescooter(user)
        else:
            menu = False
    return
def SysMenu(user):
    menu = True
    while menu == True:
        opties = Menus.system()
        Menus.toon_dynamisch_menu(opties, "Systeem Administrator")


        optie = Validator.int_input("Select option: ")
        if optie == 1:
            Gebruiker.ViewUserlist(user)
        if optie == 2:
            ServiceEngineeredit(user)  
        if optie == 3:
            TravellerMenu(user)   
        if optie == 4:
           scootermenu(user)
        if optie == 5:
            Profiles.ViewProfile(user) 
        if optie == 6:
            restore(user)
        if optie == 7:
            Databasefunctions.logs()
        else:
            SysMenu(user)


def restore(user):
    check = Validator.sanitize_input("Do you want to continue Y/N: ").upper()
    if check == "Y":
        key = Validator.sanitize_input("Key: ")
        Databasefunctions.restorebackup(user[0], key)
    else:
        return


