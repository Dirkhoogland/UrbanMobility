import Databasefunctions

def changepassword(user):
    print(f"Welkom bij password change: {user[2]}")
    nieuwpassword = input("Vul een nieuw wachtwoord in: ")

    nieuwpasswordrepeat = input("Vul het wachtwoord opnieuw in: ")

    oudpassword = input("Vul je oude wachtwoord in: ")

    if nieuwpassword == nieuwpasswordrepeat:
        check = Databasefunctions.passwordchange(user, nieuwpassword, oudpassword)

    else:
        print("Nieuwe passwords zijn niet hetzelfde")
    return



