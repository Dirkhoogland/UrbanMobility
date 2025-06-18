import sqlite3
import os

from Encrypt import Log_encrypt
from Decrypt import Log_decrypt_many

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.db")

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
        ''').fetchall()
        
    except sqlite3.OperationalError as e: 
        print(f"Failed to retrieve logs {e}")
    finally:
        if conn:
            conn.close()
        
    return Log_decrypt_many(logs)