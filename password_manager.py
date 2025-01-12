import sqlite3
from encryption import encrypt_password, decrypt_password

def add_password(user_id, service, password, key):
    try:
        encrypted_password = encrypt_password(key, password)
        conn = sqlite3.connect('password_manager.db', timeout=10)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO passwords (user_id, service, encrypted_password) VALUES (?, ?, ?)',
                       (user_id, service.lower(), encrypted_password))  # Convert service name to lowercase
        conn.commit()
        conn.close()
        print(f"Password for {service} added successfully.")
    except Exception as e:
        print(f"An error occurred during adding password: {e}")
    finally:
        if conn:
            conn.close()

def get_password(user_id, service, key):
    try:
        conn = sqlite3.connect('password_manager.db', timeout=10)
        cursor = conn.cursor()
        cursor.execute('SELECT encrypted_password FROM passwords WHERE user_id = ? AND service = ?', (user_id, service.lower()))  # Convert service name to lowercase
        result = cursor.fetchone()
        conn.close()
        if result is None:
            print("Service not found")
            return None
        encrypted_password = result[0]
        return decrypt_password(key, encrypted_password)
    except Exception as e:
        print(f"An error occurred during getting password: {e}")
    finally:
        if conn:
            conn.close()

def delete_password(user_id, service):
    try:
        conn = sqlite3.connect('password_manager.db', timeout=10)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM passwords WHERE user_id = ? AND service = ?', (user_id, service.lower()))  # Convert service name to lowercase
        conn.commit()
        conn.close()
        print(f"Password for {service} deleted successfully.")
    except Exception as e:
        print(f"An error occurred during deleting password: {e}")
    finally:
        if conn:
            conn.close()