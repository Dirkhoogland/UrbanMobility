from email.policy import default
from pickle import FALSE
import Scooter, Gebruiker , Menus , Databasefunctions , Profiles, Servicemedewerker, Validator
import Validator 
def Addservice(user):
    print("New service Engineer.")
    check = input("Do you want to continue Y/N: ")    
    check = Validator.sanitize_input(check)
    check.upper();

    if check == "Y":
        validateusername = False
        while validateusername == False:
            print("Username has to be 8-10 characters  and can only start with a _ or letter.")
            naam = input("New Engineers username: ")
            naam = Validator.sanitize_input(naam)
            validateusername = Validator.is_valid_username(naam)

        validatepassword = False
        while validatepassword == False:
            print("Password has to be 12-30 characters with:   [A-Z],[a-z] numbers [0-9] and special characters  ~!@#$%&_-+=`|\(){}[]:;'<>,.? ")
            print("The password has to be with a lower case, upper case,  cijfer and at least one speciaal character.")
            password = input("Password Engineer: ")
            password = Validator.sanitize_input(password)
            validatepassword = Validator.is_valid_password(password)

        firstname = input("User firstname: ")
        
        lastname = input("User lastname: ")

        Databasefunctions.CreateServiceMedewerker(naam, password, firstname, lastname, user)



    else:
        print("Cancelled creation")

        return
def ServiceEngineeredit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "Sys Admin edit engineer")
        optie = input("What do you want to open: ")
        optie = Validator.sanitize_input(optie)
        if optie == '1':
            Addservice(user)
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
            Profiles.ViewProfile(user) #             Gebruiker.Updatepassword(user) profiles.updateprofile()             Gebruiker.deleteaccount
        if optie == '6':
            Databasefunctions.backup(user)
        if optie == '7':
            Databasefunctions.logs()
        if optie == '8':
            menu == False
            return
        else:
            SysMenu(user)



