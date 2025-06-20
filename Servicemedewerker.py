import Scooter, Gebruiker , Menus , Databasefunctions , Profiles , Validator

def ServiceMenu(user):
    menu = True
    while menu == True:
        opties = Menus.service()
        Menus.toon_dynamisch_menu(opties, "Service medewerker")
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
        if optie == 1:
            Scooter.UpdateScooter(user)
        if optie == 2:
            Scooter.Getattributes(user)
        if optie == 3:
            Gebruiker.changepassword(user)
        if optie == 5:
            menu == False
            return






