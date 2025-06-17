import sqlite3
import os
from cryptography.fernet import Fernet
from Encrypt import get_key

def decrypt_message(token: str):
    key = get_key()
    f = Fernet(key.encode())
    message = f.decrypt(token.encode())
    return message.decode()

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

def User_decrypt(user) -> tuple:
    if user is not None:
        user = list(user)
        user[2] = decrypt_message(user[2]) 
        user = tuple(user)

    return user

def Profiles_decrypt(profile):
    if profile is not None:
        profile = list(profile)
        profile[2] = decrypt_message(profile[2])
        profile[3] = decrypt_message(profile[3])
        profile = tuple(profile)

    return profile