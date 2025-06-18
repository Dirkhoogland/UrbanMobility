import sqlite3
import os
from cryptography.fernet import Fernet


script_dir = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(script_dir, "key.txt")

def generate_key():
    key = Fernet.generate_key()
    with open(key_path, "w") as secrets_file:
        secrets_file.write(key.decode())  # Write as string
    print("Key generated and saved to key.txt")

def get_key():
    if not os.path.exists(key_path):
        print("No key found. Generating new key...")
        generate_key()

    with open(key_path, "r") as key_file:
        return key_file.read()


def encrypt_message(message: str):
    key = get_key()
    f = Fernet(key.encode())
    token = f.encrypt(message.encode())
    return token.decode()

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

def Log_encrypt(log) -> tuple:
    if log is not None:
        list(log)
        log[0] = encrypt_message(log[0])
        # log[1] = UserID
        log[2] = encrypt_message(log[2])
        log[3] = encrypt_message(log[3])
        log[4] = encrypt_message(log[4])
        log[5] = encrypt_message(log[5])
        log[6] = "Yes" if log[6] else "No"  # True is Yes otherwise False
        log[6] = encrypt_message(log[6])
        tuple(log)

    return log








