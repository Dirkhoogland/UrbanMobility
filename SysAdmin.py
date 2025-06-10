import Scooter, Gebruiker , Menus , Databasefunctions , Profiles, Servicemedewerker, Validator
import Validator 
def Addservicemedewerker(user):
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

        Databasefunctions.CreateServiceMedewerker(naam, password, firstname, lastname)



    else:
        print("Cancelled creation")

        return
def UpdateEngineer(user):
    print("Edit service Engineer.")
    check = input("Do you want to continue Y/N: ")    
    check = Validator.sanitize_input(check)
    check.upper();
    #
    if check == "Y":
        engineer = input("Which engineer: (username)")
        engineer = Validator.sanitize_input(engineer)
        data = Databasefunctions.get_user(engineer)
        if data[1] == 2:
  

            print(f" You want to edit user info: {data[2]} with Id {data[0]} and Rank {data[1]}")
            checkuser = input("Do you want to continue Y/N: ")    
            checkuser = Validator.sanitize_input(checkuser)
            checkuser.upper();


            if checkuser == "Y":
               print("You can only edit the username.")
               newusername = input("New Username: ")
               newusername = Validator.sanitize_input(newusername)
               Databasefunctions.updateServiceEngineername(engineer, newusername)

               checkforprofile = input("Do you want to update their profile? Y/N")
               checkforprofile = Validator.sanitize_input(checkforprofile)
               checkforprofile.upper();
               if checkforprofile == "Y":
                   Profiles.Updateprofile(engineer)
               else:
                    return
        else:
            print("User is not a service engineer.")
            return
def ServiceEngineeredit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "Sys Admin edit engineer")
        optie = input("What do you want to open: ")
        optie = Validator.sanitize_input(optie)
        if optie == '1':
            Addservicemedewerker(user)
        if optie == '2':
            UpdateEngineer(user)
        if optie == '3':
           Scooter.Getattributes(user)
        if optie == '4':
            Gebruiker.changepassword(user)
        if optie == '5':
            Profiles.ViewProfile(user)



def SysMenu(user):
    menu = True
    while menu == True:
        opties = Menus.system()
        Menus.toon_dynamisch_menu(opties, "Systeem Administrator")

        optie = input("What do you want to open: ")
        optie = Validator.sanitize_input(optie)
        if optie == '1':
            return
        if optie == '2':
            ServiceEngineeredit(user)         
        if optie == '3':
           Scooter.Getattributes(user)
        if optie == '4':
            Gebruiker.changepassword(user)
        if optie == '5':
            Profiles.ViewProfile(user)
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



