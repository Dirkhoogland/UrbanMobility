import Scooter, Gebruiker , Menus , Databasefunctions , Profiles, Servicemedewerker, Validator, SysAdmin
import Validator 
def AddSysteemmedewerker(user):
    print("New system Admin.")
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

        firstname = input("Gebruikers voornaam: ")
        
        lastname = input("Gebruikers lastname: ")

        Databasefunctions.CreateSysteemAdmin(naam, password, firstname, lastname)



    else:
        print("Aanmaken afgelast")

        return

def ServiceEngineeredit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "super Admin edit engineer")
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
    return
def SysteemadminEdit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "super Admin edit System Admin")
        optie = input("What do you want to open: ")
        optie = Validator.sanitize_input(optie)
        if optie == '1':
            AddSysteemmedewerker(user)
        if optie == '2':
            Gebruiker.UpdateSysteemadmin(user)
        if optie == '3':
            Gebruiker.Deleteother(user)
        if optie == '4':
            Gebruiker.changepasswordengineer(user)
        if optie == '5':
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

        optie = input("What do you want to open: ")
        optie = Validator.sanitize_input(optie)
        if optie == '1':
            Gebruiker.ViewUserlist(user)
        if optie == '2':
            Gebruiker.UpdateEngineer(user)
        if optie == '3':
           Gebruiker.Addservice(user)
        if optie == '4':
            Gebruiker.changepasswordengineer(user)
        if optie == '5':
            Profiles.ViewProfile(user)
        else:
            menu = False
            SuperMenu(user)