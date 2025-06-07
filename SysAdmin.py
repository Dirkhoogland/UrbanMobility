import Scooter, Gebruiker , Menus , Databasefunctions , Profiles, Servicemedewerker

def SysMenu(user):
    menu = True
    while menu == True:
        opties = Menus.system()
        Menus.toon_dynamisch_menu(opties, "Systeem Administrator")

        optie = input("Wat wil je openen: ")

        if optie == '1':
            ServiceMedewerker.Addservicemedewerker(user)
        if optie == '2':
            Scooter.Getattributes(user)
        if optie == '3':
            Gebruiker.changepassword(user)
        if optie == '4':
            Profiles.ViewProfile(user)
        if optie == '5':
            return 
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



