import DatabaseSetup
import Traveller
import Scooter, Gebruiker , Menus , Databasefunctions , Profiles, Servicemedewerker, Validator, SysAdmin
import Validator 

def ServiceEngineeredit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "super Admin edit engineer")
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
        if optie == 1:
            Gebruiker.Addservice(user)
        if optie == 2:
            Gebruiker.UpdateEngineer(user)
        if optie == 3:
            Gebruiker.Deleteother(user)
        if optie == 4:
            Gebruiker.changepasswordengineer(user)
        if optie == 5:
            Profiles.ViewProfile(user)
        else:
            menu = False
    return

def SysteemadminEdit(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.Servicemedewerkeropties()
        Menus.toon_dynamisch_menu(optiesmenu, "super Admin edit System Admin")
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
        if optie == 1:
            Gebruiker.AddSysteemmedewerker(user)
        if optie == 2:
            Gebruiker.UpdateSysteemadmin(user)
        if optie == 3:
            Gebruiker.Deleteother(user)
        if optie == 4:
            Gebruiker.changepasswordengineer(user)
        if optie == 5:
            Profiles.ViewProfile(user)
        else:
            menu = False
    return

def scootermenu(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.scooterinfo(user[1])
        Menus.toon_dynamisch_menu(optiesmenu, "super Admin edit scooter ")
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
        if optie == 1:
            Scooter.UpdateScooteradmin(user)
        if optie == 2:
            Scooter.Getattributes(user)
        if optie == 3:
            Scooter.newscooter(user)
        if optie == 4:
            Scooter.Deletescooter(user)
        else:
            menu = False
    return


def Revokekey():
    print("Welcome to key removal super admin")
    menu = True
    while menu == True:
        try:
                optie = int(input("Which user id?: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
        Databasefunctions.Revokekey(optie)
        menu = False


def BackupMenu(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.backups()
        Menus.toon_dynamisch_menu(optiesmenu, "super Admin backupmenu ")
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
        if optie == 1: 
            Databasefunctions.Createbackupkey(1, "Superadmin", "Superadmin") # doneuser_id, backup_namen, key_value
        if optie == 2:
            DatabaseSetup.CreateBackupKey() # done
        if optie == 3:
            Databasefunctions.restorebackup(1, "Superadmin")
        if optie == 4:
            Revokekey()
        else:
            menu = False
    return

def TravellerMenu(user):
    menu = True
    while menu == True:
        optiesmenu = Menus.addmodifytravellers()
        Menus.toon_dynamisch_menu(optiesmenu, "Systeem Admin edit scooter ")
        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue
        if optie == 1:
            Traveller.AddTraveller(user)
        if optie == 2:
            Traveller.Update(user)
        if optie == 3:
            Email = Validator.sanitize_input("Gebruiker Email:")
            Traveller.View(Email, user)
        if optie == 4:
            Traveller.Delete(user)
        else:
            menu = False
    return
def SuperMenu(user):
    menu = True
    while menu == True:
        opties = Menus.super()
        Menus.toon_dynamisch_menu(opties, "Super Admin")

        try:
                optie = int(input("Select option: "))
        except ValueError:
                print("invalid input, choose a number.")
                continue

        if optie == 1:
            Gebruiker.ViewUserlist(user)
        if optie == 2:
            SysteemadminEdit(user)
        if optie == 3:
            ServiceEngineeredit(user)
        if optie == 4:
            TravellerMenu(user) 
        if optie == 5:
            scootermenu(user) 
        if optie == 6:
            BackupMenu(user) 
        if optie == 7:
            Databasefunctions.logs()
        else:
            menu = False
            SuperMenu(user)