import Databasefunctions, Menus , Validator, UrbanMobility, Profiles
def Addservice(user):
    print("New service Engineer.")
    
    check = Validator.sanitize_input("Do you want to continue Y/N: ")
    check.upper();

    if check == "Y":
        validateusername = False
        while validateusername == False:
            print("Username has to be 8-10 characters  and can only start with a _ or letter.")

            naam = Validator.sanitize_input("New Engineers username: ")
            validateusername = Validator.is_valid_username(naam)

        validatepassword = False
        while validatepassword == False:
            print(r"Password has to be 12-30 characters with:   [A-Z],[a-z] numbers [0-9] and special characters  ~!@#$%&_-+=`|\(){}[]:;'<>,.? ")
            print("The password has to be with a lower case, upper case,  cijfer and at least one speciaal character.")

            password = Validator.sanitize_input("Password Engineer: ")
            validatepassword = Validator.is_valid_password(password)

        firstname = Validator.sanitize_input("User firstname: ")
        
        lastname = Validator.sanitize_input("User lastname: ")

        Databasefunctions.CreateServiceMedewerker(naam, password, firstname, lastname, user)


    else:
        print("Cancelled creation")

        return


def AddSysteemmedewerker(user):
    print("New service Engineer.")
    
    check = Validator.sanitize_input("Do you want to continue Y/N: ")
    check.upper();

    if check == "Y":
        validateusername = False
        while validateusername == False:
            print("Username has to be 8-10 characters  and can only start with a _ or letter.")

            naam = Validator.sanitize_input("New Engineers username: ")
            validateusername = Validator.is_valid_username(naam)

        validatepassword = False
        while validatepassword == False:
            print(r"Password has to be 12-30 characters with:   [A-Z],[a-z] numbers [0-9] and special characters  ~!@#$%&_-+=`|\(){}[]:;'<>,.? ")
            print("The password has to be with a lower case, upper case,  cijfer and at least one speciaal character.")

            password = Validator.sanitize_input("Password Engineer: ")
            validatepassword = Validator.is_valid_password(password)

        firstname = Validator.sanitize_input("User firstname: ")
        
        lastname = Validator.sanitize_input("User lastname: ")

        Databasefunctions.CreateSysteemAdmin(naam, password, firstname, lastname, user)
def changepassword(user):
    print(f"Welcome to change password: {user[2]}")


    nieuwpassword = Validator.sanitize_input("New Password: ")


    nieuwpasswordrepeat = Validator.sanitize_input("Repeat new password: ")


    oudpassword = Validator.sanitize_input("Old password: ")

    if nieuwpassword == nieuwpasswordrepeat:
        check = Databasefunctions.passwordchange(user, nieuwpassword, oudpassword)

    else:
        print("new passwords are not the same")
    return

def changepasswordengineer(user):
    print("Change password for service Engineer.")
    
    check = Validator.sanitize_input("Do you want to continue Y/N: ")
    check.upper();
    
    if check == "Y":

        engineer = Validator.sanitize_input("Which engineer: (username)")
        data = Databasefunctions.get_user(engineer)
        if data[1] == 2:


            nieuwpassword = Validator.sanitize_input("New Password: ")


            nieuwpasswordrepeat = Validator.sanitize_input("Repeat new password: ")
            check = input("Type CONFIRM to confirm: ")

            check = Validator.sanitize_input(check)
            if check == 'CONFIRM':
             Databasefunctions.passwordchangeengineer(data, nieuwpassword, user)


        else:
            print("User is not a service engineer.")
            return
def ViewUserlist(user):
    print(f"Welcome to userlogs: {user[2]}")
    Users = Databasefunctions.get_users(user)
    Menus.toon_dynamisch_menu(Users, "User logs")
    input( "Press enter to continue . . .")
    return 

def Deleteuser(user):
    print(f"Are you sure you want to delete your account: {user[2]}")


    check = Validator.sanitize_input("Type CONFIRM to confirm: ")
    if check == 'CONFIRM':
        Databasefunctions.Deleteaccountown(user)
        UrbanMobility.Start()
    else:
        print("Deletion aborted")

    return

def Deleteother(user):
    print("Delete service Engineer.")
  
    check = Validator.sanitize_input("Do you want to continue Y/N: ")
    check.upper();
    
    if check == "Y":
        engineer = Validator.sanitize_input("Which engineer: (username)")
        data = Databasefunctions.get_user(engineer)
        if data[1] == 2:
           print(f"Are you sure you want to delete account: {engineer}")


           check = Validator.sanitize_input("Type CONFIRM to confirm: ")
           if check == 'CONFIRM':
             Databasefunctions.Deleteaccount(data, user)

        else:
            print("User is not a service engineer.")
            return

def UpdateEngineer(user):
    print("Edit service Engineer.")
   
    check = Validator.sanitize_input("Do you want to continue Y/N: ")
    check.upper();
    
    if check == "Y":

        engineer = Validator.sanitize_input("Which engineer: (username)")
        data = Databasefunctions.get_user(engineer)
        if data[1] == 2:
  

            print(f" You want to edit user info: {data[2]} with Id {data[0]} and Rank {data[1]}")  
            checkuser = Validator.sanitize_input("Do you want to continue Y/N: ")
            checkuser.upper();


            if checkuser == "Y":
               print("You can only edit the username.")
               newusername = Validator.sanitize_input("New Username: ")
               Databasefunctions.updateServiceEngineername(engineer, newusername)


               checkforprofile = Validator.sanitize_input("Do you want to update their profile? Y/N")
               checkforprofile.upper();
               if checkforprofile == "Y":
                   Profiles.Updateprofile(engineer)
               else:
                    return
        else:
            print("User is not a service engineer.")
            return


def UpdateSysteemadmin(user):
    print("Edit System Admin.")
    check = Validator.sanitize_input("Do you want to continue Y/N: ")
    check.upper();
    
    if check == "Y":
        engineer = Validator.sanitize_input("Which System Admin: (username)")
        data = Databasefunctions.get_user(engineer)
        if data[1] == False:
  

            print(f" You want to edit user info: {data[2]} with Id {data[0]} and Rank {data[1]}")
  
            checkuser = Validator.sanitize_input("Do you want to continue Y/N: ")
            checkuser.upper();


            if checkuser == "Y":
               print("You can only edit the username.")

               newusername = Validator.sanitize_input("New Username: ")
               Databasefunctions.updateSystemAdminname(engineer, newusername)


               checkforprofile = Validator.sanitize_input("Do you want to update their profile? Y/N")
               checkforprofile.upper();
               if checkforprofile == "Y":
                   Profiles.Updateprofile(engineer)
               else:
                    return
        else:
            print("User is not a System Admin.")
            return

def UpdatePasswordSysteemadmin(user):
    print("Change password for System Admin.")
  
    check = Validator.sanitize_input("Do you want to continue Y/N: ")
    check.upper();
    
    if check == "Y":

        engineer = Validator.sanitize_input("Which System Admin: (username)")
        data = Databasefunctions.get_user(engineer)
        if data[1] == 1:


            nieuwpassword = Validator.sanitize_input("New Password: ")


            nieuwpasswordrepeat = Validator.sanitize_input("Repeat new password: ")


            check = Validator.sanitize_input("Type CONFIRM to confirm: ")
            if check == 'CONFIRM':
             Databasefunctions.passwordchangeengineer(data, nieuwpassword, user)


        else:
            print("User is not a System Admin.")
            return