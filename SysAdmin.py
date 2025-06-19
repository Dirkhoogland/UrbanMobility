from email.policy import default
from pickle import FALSE
import Traveller
import Scooter, Gebruiker , Menus , Databasefunctions , Profiles, Servicemedewerker, Validator
import Validator 

def ServiceEngineeredit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "Sys Admin edit engineer")

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
            SysMenu(user)


def TravellerMenu(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.addmodifytravellers()
        Menus.toon_dynamisch_menu(optiesmenu, "Systeem Admin edit scooter ")
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
        if optie == 1:
            Traveller.AddTraveller(user)
        if optie == 2:
            Traveller.Update(user)
        if optie == 3:
            Email = Validator.sanitize_input("Gebruiker Email:")
            Traveller.View(Email, user)
        if optie == 4:
            Traveller.Delete(user)
        else:
            menu = False
    return
# ["Add new Traveller", "Update Traveller in system", "Delete a traveller", "Search Traveller"]
def scootermenu(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.TravelerUpdateOptions(user[1])
        Menus.toon_dynamisch_menu(optiesmenu, "Systeem Admin edit Traveller ")
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
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


        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
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
        if optie == 8:
            menu == False
            return
        else:
            SysMenu(user)


def restore(user):

       
    check = Validator.sanitize_input("Do you want to continue Y/N: ")
    check.upper();
    key = Validator.sanitize_input("Key: ")
    if check == "Y":

        Databasefunctions.restorebackup(user[0], key)
    else:
        return


