import Databasefunctions, Menus , Validator, UrbanMobility, Profiles

def changepassword(user):
    print(f"Welcome to change password: {user[2]}")

    nieuwpassword = input("New Password: ")
    nieuwpassword = Validator.sanitize_input(nieuwpassword)

    nieuwpasswordrepeat = input("Repeat new password: ")
    nieuwpasswordrepeat = Validator.sanitize_input(nieuwpasswordrepeat)

    oudpassword = input("Old password: ")
    oudpassword = Validator.sanitize_input(oudpassword)

    if nieuwpassword == nieuwpasswordrepeat:
        check = Databasefunctions.passwordchange(user, nieuwpassword, oudpassword)

    else:
        print("new passwords are not the same")
    return

def changepasswordengineer(user):
    print("Change password for service Engineer.")
    check = input("Do you want to continue Y/N: ")    
    check = Validator.sanitize_input(check)
    check.upper();
    
    if check == "Y":
        engineer = input("Which engineer: (username)")
        engineer = Validator.sanitize_input(engineer)
        data = Databasefunctions.get_user(engineer)
        if data[1] == 2:

            nieuwpassword = input("New Password: ")
            nieuwpassword = Validator.sanitize_input(nieuwpassword)

            nieuwpasswordrepeat = input("Repeat new password: ")
            nieuwpasswordrepeat = Validator.sanitize_input(nieuwpasswordrepeat)
            check = input("Type CONFIRM to confirm: ")

            check = Validator.sanitize_input(check)
            if check == 'CONFIRM':
             Databasefunctions.passwordchangeengineer(user, nieuwpassword)


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
    check = input("Type CONFIRM to confirm: ")

    check = Validator.sanitize_input(check)
    if check == 'CONFIRM':
        Databasefunctions.Deleteaccount(user)
        UrbanMobility.Start()
    else:
        print("Deletion aborted")

    return

def Deleteother(user):
    print("Delete service Engineer.")
    check = input("Do you want to continue Y/N: ")    
    check = Validator.sanitize_input(check)
    check.upper();
    
    if check == "Y":
        engineer = input("Which engineer: (username)")
        engineer = Validator.sanitize_input(engineer)
        data = Databasefunctions.get_user(engineer)
        if data[1] == 2:
           print(f"Are you sure you want to delete account: {engineer}")
           check = input("Type CONFIRM to confirm: ")

           check = Validator.sanitize_input(check)
           if check == 'CONFIRM':
             Databasefunctions.Deleteaccount(data, user)

        else:
            print("User is not a service engineer.")
            return

def UpdateEngineer(user):
    print("Edit service Engineer.")
    check = input("Do you want to continue Y/N: ")    
    check = Validator.sanitize_input(check)
    check.upper();
    
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
