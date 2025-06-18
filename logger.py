import sqlite3
from DatabaseSetup import db_path

from Encrypt import Log_encrypt
from Decrypt import Log_decrypt_many

def Encrypt_Log(Action, UserID, Username, Timestamp, Result, Serverity, Sus: bool):
    return Log_encrypt(Action, UserID, Username, Timestamp, Result, Serverity, Sus)

def Decrypte_all_logs():
    conn = None
    logs = []

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        logs = cursor.execute('''
            SELECT * FROM ActionLog
        )''').fetchall()

    except sqlite3.OperationalError: 
        print("Failed to retrieve logs")
    finally:
        if conn:
            conn.close()
        return Log_decrypt_many(logs)