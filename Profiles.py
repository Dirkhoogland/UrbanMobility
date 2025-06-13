import Databasefunctions, Validator, Menus , Gebruiker

def ViewProfile(user):


    profiel = Databasefunctions.searchprofile(user[0])
    print(f"Firstname: {profiel[2]}")
    print(f"Lastname: {profiel[3]}")
    print(f"Registrationdate: {profiel[4]}")

    menu = True
    while menu == True:
        opties = Menus.profiles()
        Menus.toon_dynamisch_menu(opties, "Profile menu")

        optie = input("What do you want to open: ")
        optie = Validator.sanitize_input(optie)
        if optie == '1':
            Updateprofile(user, user[0])
        if optie == '2':
            Gebruiker.changepassword(user)      
        if optie == '3':
           Gebruiker.Deleteuser(user)

    #input("Druk op Enter om door te gaan...")
    # return profiel


def Updateprofile(user, id):
    print("User profile")
    profile = ViewProfile(id)

    checkuser = input("Do you want to continue Y/N: ")    
    checkuser = Validator.sanitize_input(checkuser)
    checkuser.upper();
    username = profile[2]
    Newlastname = profile[3]
    if checkuser == "Y":
        print("Leave empty if it does not need to be updated")
        Newusername = input("New Firstname:")
        Newusername = Validator.sanitize_input(Newusername)
        Newlastname = input("New Lastname: ")
        Newlastname = Validator.sanitize_input(Newlastname)
        if Newusername:
            username = Newusername
        if Newlastname:
            lastname = Newlastname

        Databasefunctions.updateprofile(username, lastname, profile[0], user)






