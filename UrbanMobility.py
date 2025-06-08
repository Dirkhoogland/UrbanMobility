import DatabaseSetup
import Databasefunctions
import Menus , Servicemedewerker, SysAdmin, Superadmin
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
        # username = input("Vul je username in: ")
        username = "super_admin"
        # password = input("Vul je password in: ")
        password = "Admin_123?"
        check = Databasefunctions.login(username, password)
        if check == True: 
            login = False
    # gets rank number and name
    user = Databasefunctions.getuserdetails(username)
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

            



        # Admin:
        # 1. Add/modify Service Engineer
        # 2. Check Users
        # 3. Update Scooter
        # 4. Get Scooter attributes
        # 5. Update Password
        # 6. Logout
        
        # Admin
        # if user[1] == 0:
        #     AdminOptions()

        # if user[1] == 1 
        # 
        # if user[1] == 2:


        # User?
        # if user == 1:
        #     if opties == 1:

        #     if opties == 2:

        #     if opties == 3:

        # ServiceMedewerker
        # if user[2] == 2:
        #     if opties == 1:

        #     if opties == 2:

        #     if opties == 3:

    # def AdminOptions(choice):
        # if choice == 1:
            
        # if choice == 2:
        
        # if choice == 3:

        # if choice == 4:

        # if choice == 5:

        # if choice == 6:

    # def ServiceOptions(choice):
        # if choice == 1:

        # if choice == 2:

        # if choice == 3:

        # if choice == 4: