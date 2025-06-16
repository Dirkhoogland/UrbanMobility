import sqlite3
import os
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("key.txt", "w") as secrets_file:
        secrets_file.write(key.decode())  # Write as string
    print("Key generated and saved to key.txt")

def get_key():
    if not os.path.exists("key.txt"):
        print("No key found. Generating new key...")
        generate_key()

    with open("key.txt", "r") as key_file:
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
def traveller_decrypt(traveller: tuple) -> tuple:
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
            travellers[i] = traveller_decrypt(travellers[i])
            i += 1

    return travellers


