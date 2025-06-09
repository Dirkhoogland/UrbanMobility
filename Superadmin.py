import Scooter, Gebruiker , Menus , Databasefunctions , Profiles, Servicemedewerker, Validator, SysAdmin
import Validator 
def Addservicemedewerker(user):
    print("Nieuwe service medewerker aan maken.")
    check = input("Wil je door gaan Y/N: ")    
    check = Validator.sanitize_input(check)
    check.upper();

    if check == "Y":
        validateusername = False
        while validateusername == False:
            print("Username moet 8-10 karakters zijn en kan alleen beginnen met een _ of letter.")
            naam = input("Nieuwe gebruiker user name: ")
            naam = Validator.sanitize_input(naam)
            validateusername = Validator.is_valid_username(naam)

        validatepassword = False
        while validatepassword == False:
            print("Password moet 12-30 karacters zijn met letters [A-Z],[a-z] cijfers [0-9] en speciale tekens  ~!@#$%&_-+=`|\(){}[]:;'<>,.? ")
            print("Het password moet ook een lower case, een upper case, een cijfer en een speciaal teken hebben.")
            password = input("Wachtwoord gebruiker: ")
            password = Validator.sanitize_input(password)
            validatepassword = Validator.is_valid_password(password)

        firstname = input("Gebruikers voornaam: ")
        
        lastname = input("Gebruikers lastname: ")

        Databasefunctions.CreateServiceMedewerker(naam, password, firstname, lastname)



    else:
        print("Aanmaken afgelast")

        return


def AddSysteemmedewerker(user):
    print("Nieuwe Systeem Administrator aan maken.")
    check = input("Wil je door gaan Y/N: ")    
    check = Validator.sanitize_input(check)
    check.upper();

    if check == "Y":
        validateusername = False
        while validateusername == False:
            print("Username moet 8-10 karakters zijn en kan alleen beginnen met een _ of letter.")
            naam = input("Nieuwe gebruiker user name: ")
            naam = Validator.sanitize_input(naam)
            validateusername = Validator.is_valid_username(naam)

        validatepassword = False
        while validatepassword == False:
            print("Password moet 12-30 karacters zijn met letters [A-Z],[a-z] cijfers [0-9] en speciale tekens  ~!@#$%&_-+=`|\(){}[]:;'<>,.? ")
            print("Het password moet ook een lower case, een upper case, een cijfer en een speciaal teken hebben.")
            password = input("Wachtwoord gebruiker: ")
            password = Validator.sanitize_input(password)
            validatepassword = Validator.is_valid_password(password)

        firstname = input("Gebruikers voornaam: ")
        
        lastname = input("Gebruikers lastname: ")

        Databasefunctions.CreateSysteemAdmin(naam, password, firstname, lastname)



    else:
        print("Aanmaken afgelast")

        return

def SuperMenu(user):
    menu = True
    while menu == True:
        opties = Menus.super()
        Menus.toon_dynamisch_menu(opties, "Super Admin")

        optie = input("Wat wil je openen: ")
        optie = Validator.sanitize_input(optie)
        if optie == '1':
            Addservicemedewerker(user)
        if optie == '2':
            AddSysteemmedewerker(user)
        if optie == '3':
            Gebruiker.changepassword(user)
        if optie == '4':
            Profiles.ViewProfile(user)
        if optie == '5':
            return 
        if optie == '6':
            return 
        if optie == '7':
            return 
        if optie == '8':
            return 
        if optie == '9':
            return 
        if optie == '10':
            return 
        if optie == '11':
            return 
        if optie == '12':
            menu == False
            return