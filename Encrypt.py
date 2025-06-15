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
        # traveller[0] is Id
        traveller[1] = encrypt_message(traveller[1]) # Firstname
        traveller[2] = encrypt_message(traveller[2]) # Lastname
        traveller = tuple(traveller)

    return traveller

def Traveller_decrypt_many(travellers): # -> list<tuple>
    if travellers is not None:
        i = 0
        while i < len(travellers): # equavelent of Count in C#
            travellers[i] = traveller_decrypt(travellers[i])
            i += 1

    return travellers
