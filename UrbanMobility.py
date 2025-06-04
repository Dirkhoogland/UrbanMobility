import DatabaseSetup
import Databasefunctions
import Menus , Servicemedewerker
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


def start():
    login = True;
    while login == True:
        username = input("Vul je username in: ")

        password = input("Vul je password in: ")
    
        check = Databasefunctions.login(username, password)
        if check == True: 
            login = False
    # gets rank number and name
    user = Databasefunctions.getuserdetails(username)
    # plaatst het in een naam die gebruikelijk is voor de user
    ranking = getuserrank(user[0]);
    print(f"Welkom bij het UrbanMobility project {user[1]} rank {ranking}")

    mainmenu = True
    while mainmenu == True:
        print(f"Hallo {ranking} {user[1]} ")

        opties = " "
        if user[0] == 0:
            opties = Menus.super()
        if user == 1:
            opties = Menus.system()
        if user[0] == 2:
            Servicemedewerker.ServiceMenu(user)

        



start();