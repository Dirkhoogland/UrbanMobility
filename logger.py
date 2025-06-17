import sqlite3
from DatabaseSetup import db_path

from Encrypt import Log_encrypt
from Decrypt import Log_decrypt_many

def AddLog(Action, UserID, Username, Timestamp, Result, Serverity, Sus: bool):
    return Log_encrypt(Action, UserID, Username, Timestamp, Result, Serverity, Sus)

def decrypte_all_logs(logs):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    logs = cursor.execute('''
        SELECT * FROM ActionLog
    )''')
    conn.close()
    return Log_decrypt_many(logs)