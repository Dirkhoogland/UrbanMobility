import DatabaseSetup
import Databasefunctions
import Menus , Servicemedewerker, SysAdmin, Superadmin, Validator
from Menus import toon_dynamisch_menu
# programming debug for editing db
# DatabaseSetup.Databasesetupstart()

startup = True;

def getuserrank(rank):
    if rank == 0:
        return "Super Administrator"
    if rank == 1:
        return "System Administrator"
    if rank == 2:
        return "Service Engineer"

def Start():
    login = True;
    while login == True:
        # username =  Validator.sanitize_input("Vul je username in: ")

        username = "_jan.01"
 
        # password =  Validator.sanitize_input("Vul je password in: ")

        password = "S3cure#Pass!12"

        user = Databasefunctions.login(username, password)
        if user != False: 
            login = False
    # gets rank number and name
    #user = Databasefunctions.getuserdetails(username)
    # plaatst het in een naam die gebruikelijk is voor de user
    ranking = getuserrank(user[1]);
    print(f"Welkom bij het UrbanMobility project {user[2]} rank {ranking}")

    mainmenu = True
    while mainmenu == True:
        print(f"Hallo {ranking} {user[2]} ")
        print()

        if user[1] == 0:
            Superadmin.SuperMenu(user)
            
        if user[1] == 1:
            SysAdmin.SysMenu(user)

        if user[1] == 2:
            Servicemedewerker.ServiceMenu(user)
