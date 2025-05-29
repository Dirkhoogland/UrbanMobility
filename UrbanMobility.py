import DatabaseSetup
import Databasefunctions

DatabaseSetup.Databasesetupstart()

startup = True;

def start():
    login = True;
    while login == True:
        username = input("Vul je username in: ")

        password = input("Vul je password in: ")
    
        check = Databasefunctions.login(username, password)
        if check == True: 
            login = False

    user = Databasefunctions.getuserdetails(username)
    print(f"Welkom bij het UrbanMobility project {user[1]} rank {user[0]}")



start();