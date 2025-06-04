import Databasefunctions
import Menus
import Scooter

def ServiceMenu(user):
        opties = Menus.service()
        Menus.toon_dynamisch_menu(opties)

        optie = input("Wat wil je openen")
        lengte = opties.__len__()
        print(lengte)
        if optie == 1:
            Scooter.UpdateScooter(user)
        if optie == 2:
            Scooter.Getattributes(user)
        # if optie == 3:
        #     gebruiker.UpdatePassword(user)
        if optie == 4:
            return




