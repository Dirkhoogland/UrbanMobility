import DatabaseSetup
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
            DatabaseSetup.CreateBackup() # done
        if optie == 2:
            DatabaseSetup.CreateBackupKey() # done
        if optie == 3:
            DatabaseSetup.Useownbackup()
        if optie == 4:
            DatabaseSetup.Revokekey()
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
            Gebruiker.changepasswordengineer(user) # change to traveller
        if optie == 5:
            scootermenu(user) # no create or delete
        if optie == 6:
            access_password(user) # no codes yet/functions
        if optie == 7:
            DatabaseSetup.CreateBackup() # doesnt work yet
        if optie == 8:
            Databasefunctions.logs()
        else:
            menu = False
            SuperMenu(user)