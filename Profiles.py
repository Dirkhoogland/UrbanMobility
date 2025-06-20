from Decrypt import Profiles_decrypt
import Databasefunctions, Validator, Menus , Gebruiker

def ViewProfile(user):


    profiel = Databasefunctions.searchprofile(user)
    print(f"Firstname: {profiel[2]}")
    print(f"Lastname: {profiel[3]}")
    print(f"Registrationdate: {profiel[4]}")

    menu = True
    while menu == True:
        opties = Menus.profiles()
        Menus.toon_dynamisch_menu(opties, "Profile menu")
        int_input("Select option: ")
        if optie == 1:
            Updateprofile(user, user[0])
        if optie == 2:
            Gebruiker.changepassword(user)      
        if optie == 3:
           Gebruiker.Deleteuser(user)

    #input("Druk op Enter om door te gaan...")
    # return profiel

def updateview(id):

    profiel = Databasefunctions.searchprofile(id)
    print(f"Firstname: {profiel[2]}")
    print(f"Lastname: {profiel[3]}")
    print(f"Registrationdate: {profiel[4]}")
    return profiel


def Updateprofile(user, id):
    print("User profile")
    profile = updateview(id)

 
    checkuser = Validator.sanitize_input("Do you want to continue Y/N: ").upper();

    username = profile[2]
    Newlastname = profile[3]
    opties = ["Firstname", "Lastname", "Leave menu"]
    if checkuser == "Y":
     menu = True
     while menu == True:
        Menus.toon_dynamisch_menu(opties, "Profile menu")
        int_input("Select option: ")
        if optie == 1:
             Newusername = Validator.sanitize_input("New Firstname:")
             Databasefunctions.updateprofilfirstnamee(id, Newusername, user)
        if optie == 2:
            Newlastname = Validator.sanitize_input("New Lastname: ") 
            Databasefunctions.updateprofilelastname(id, Newlastname, user)
        if optie == 3:
           menu = False
           return







