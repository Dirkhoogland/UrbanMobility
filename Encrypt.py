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
    return token


def decrypt_message(token: bytes):
    key = get_key()
    f = Fernet(key.encode())
    message = f.decrypt(token)
    return message.decode()


def test_key_demo():
    message = "This is a secret message"
    print("\nOriginal message:", message)

    encrypted = encrypt_message(message)
    print("Encrypted:", encrypted)

    decrypted = decrypt_message(encrypted)
    print("Decrypted:", decrypted)
    
    