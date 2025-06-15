import sqlite3
import os
from cryptography.fernet import Fernet  # Fixed spelling and case

# import site
# import sys

# print(site.getsitepackages())
# print(sys.path)


# def GetSecreteKey():
#     try:
#         with open("secret.txt", "r") as secrets_file:
#             return secrets_file.read()
#     except:
#         print("No key found generating new key")
    
    
# key = GetSecreteKey()

# def GenerateKey():
#     key = Fernet.Generate_key
#     with open("secret.txt", "r") as secrets_file:
#         key = secrets_file.read()
#     engine = Fernet(key)

def test_Key_Demo(string):
    # Put this somewhere safe!
    key = Fernet.generate_key()
    key2 = Fernet.generate_key()
    f = Fernet(key)
    k = Fernet(key2)
    string = string.encode("utf-8")
    token = f.encrypt(string)
    print(token)
    token = f.decrypt(token)
    print(token)
    token = k.encrypt(token)
    print(token)
    token = k.decrypt(token)
    print(token)

    
    