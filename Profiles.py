import Databasefunctions, Validator

def ViewProfile(user):


    profiel = Databasefunctions.searchprofile(user[0])
    print(f"Firstname: {profiel[2]}")
    print(f"Lastname: {profiel[3]}")
    print(f"Registrationdate: {profiel[4]}")

    input("Druk op Enter om door te gaan...")
    return profiel


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

        Databasefunctions.updateprofile(username, lastname, profile[0])






