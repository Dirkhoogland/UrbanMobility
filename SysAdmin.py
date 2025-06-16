from email.policy import default
from pickle import FALSE
import Scooter, Gebruiker , Menus , Databasefunctions , Profiles, Servicemedewerker, Validator
import Validator 

def ServiceEngineeredit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "Sys Admin edit engineer")
        optie = input("What do you want to open: ")
        optie = Validator.sanitize_input(optie)
        if optie == '1':
            Gebruiker.Addservice(user)
        if optie == '2':
            Gebruiker.UpdateEngineer(user)
        if optie == '3':
            Gebruiker.Deleteother(user)
        if optie == '4':
            Gebruiker.changepasswordengineer(user)
        if optie == '5':
            Profiles.ViewProfile(user)
        else:
            menu = False
            SysMenu(user)



def SysMenu(user):
    menu = True
    while menu == True:
        opties = Menus.system()
        Menus.toon_dynamisch_menu(opties, "Systeem Administrator")

        optie = input("What do you want to open: ")
        optie = Validator.sanitize_input(optie)
        if optie == '1':
            Gebruiker.ViewUserlist(user)
        if optie == '2':
            ServiceEngineeredit(user)  
        if optie == '3':
            ServiceEngineeredit(user)   
        if optie == '4':
           Scooter.Getattributes(user)
        if optie == '5':
            Profiles.ViewProfile(user) 
        if optie == '6':
            Databasefunctions.backup(user)
        if optie == '7':
            Databasefunctions.logs()
        if optie == '8':
            menu == False
            return
        else:
            SysMenu(user)



