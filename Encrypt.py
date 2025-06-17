import sqlite3
import os
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("UrbanMobility/key.txt", "w") as secrets_file:
        secrets_file.write(key.decode())  # Write as string
    print("Key generated and saved to key.txt")

def get_key():
    if not os.path.exists("UrbanMobility/key.txt"):
        print("No key found. Generating new key...")
        generate_key()

    with open("UrbanMobility/key.txt", "r") as key_file:
        return key_file.read()


def encrypt_message(message: str):
    key = get_key()
    f = Fernet(key.encode())
    token = f.encrypt(message.encode())
    return token.decode()


def decrypt_message(token: str):
    key = get_key()
    f = Fernet(key.encode())
    message = f.decrypt(token.encode())
    return message.decode()

def Traveller_encrypt(traveller: tuple) -> tuple:
    if traveller is not None:
        traveller = list(traveller)
        traveller[0] = encrypt_message(traveller[0]) # Firstname
        traveller[1] = encrypt_message(traveller[1]) # Lastname
        traveller[4] = encrypt_message(traveller[4]) # Streetname
        traveller[6] = encrypt_message(traveller[6]) # Zipcode
        traveller[8] = encrypt_message(traveller[8]) # Email
        traveller[9] = encrypt_message(traveller[9]) # phonenumber
        traveller[10] = encrypt_message(traveller[10]) # DLN
        traveller = tuple(traveller)

    return traveller

def Traveller_encrypt_many(travellers): # -> list<tuple>
    if travellers is not None:
        i = 0
        while i < len(travellers): # equavelent of Count in C#
            travellers[i] = Traveller_encrypt(travellers[i])
            i += 1

    return travellers

# Used in View also includes ID collum so indexing is diffrent 
def Traveller_decrypt(traveller: tuple) -> tuple:
    if traveller is not None:
        traveller = list(traveller)
        traveller[1] = decrypt_message(traveller[1]) # Firstname
        traveller[2] = decrypt_message(traveller[2]) # Lastname
        traveller[5] = decrypt_message(traveller[5]) # Streetname
        traveller[7] = decrypt_message(traveller[7]) # Zipcode
        traveller[9] = decrypt_message(traveller[9]) # Email
        traveller[10] = decrypt_message(traveller[10]) # phonenumber
        traveller[11] = decrypt_message(traveller[11]) # DLN
        
        traveller = tuple(traveller)

    return traveller

def Traveller_decrypt_many(travellers): # -> list<tuple>
    if travellers is not None:
        i = 0
        while i < len(travellers): # equavelent of Count in C#
            travellers[i] = Traveller_decrypt(travellers[i])
            i += 1

    return travellers

def Users_encrypt(user) -> tuple:
    if user is not None:
        user = list(user)
        user[1] = encrypt_message(user[1]) 
        user = tuple(user)
        pass

    return user

def Users_encrypt_many(users): # -> list<tuple>
    if users is not None:
        i = 0
        while i < len(users):
            users[i] = Users_encrypt(users[i])
            i += 1

    return users

def User_decrypt(user) -> tuple:
    if user is not None:
        user = list(user)
        user[2] = decrypt_message(user[2]) 
        user = tuple(user)

    return user


def Profiles_encrypt_many(profiles): # -> list<tuple>
    if profiles is not None:
        i = 0
        while i < len(profiles):
            profiles[i] = Profiles_encrypt(profiles[i])
            i += 1

    return profiles


def Profiles_encrypt(profile) -> tuple: 
    if profile is not None:
        profile = list(profile)
        # profile[NONE] = ID
        # profile[0] = UserID
        profile[1] = encrypt_message(profile[1])
        profile[2] = encrypt_message(profile[2])
        profile = tuple(profile)
        # profile[3] = RegistrationDate

    return profile

def Profiles_decrypt(profile):
    if profile is not None:
        profile = list(profile)
        profile[2] = decrypt_message(profile[2])
        profile[3] = decrypt_message(profile[3])
        profile = tuple(profile)

    return profile








