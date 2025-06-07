import Databasefunctions

def ViewProfile(user):


    profiel = Databasefunctions.searchprofile(user[0])
    print(f"Voornaam: {profiel[2]}")
    print(f"Achternaam: {profiel[3]}")
    print(f"Registratiedatum: {profiel[4]}")

    input("Druk op Enter om door te gaan...")




