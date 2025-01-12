import sqlite3
import bcrypt
from encryption import encrypt_password, decrypt_password, load_key

def register(username, password):
    try:
        conn = sqlite3.connect('password_manager.db', timeout=10)
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        key = load_key()
        password_hash = encrypt_password(key, hashed_password.decode())
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username.lower(), password_hash))
        conn.commit()
        conn.close()
        print(f"User {username} registered successfully.")
        return True
    except sqlite3.IntegrityError:
        print("Username already exists")
    except Exception as e:
        print(f"An error occurred during registration: {e}")
    finally:
        if conn:
            conn.close()
    return False

def login(username, password):
    try:
        conn = sqlite3.connect('password_manager.db', timeout=10)
        cursor = conn.cursor()
        cursor.execute('SELECT id, password_hash FROM users WHERE username = ?', (username.lower(),))
        result = cursor.fetchone()
        if result is None:
            print("Username not found")
            return None
        user_id, password_hash = result
        key = load_key()
        decrypted_password_hash = decrypt_password(key, password_hash).encode()
        if bcrypt.checkpw(password.encode(), decrypted_password_hash):
            print(f"User {username} logged in successfully.")
            return user_id
        else:
            print("Incorrect password")
    except Exception as e:
        print(f"An error occurred during login: {e}")
    finally:
        if conn:
            conn.close()
    return None

def change_password(user_id, new_password):
    try:
        conn = sqlite3.connect('password_manager.db', timeout=10)
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        key = load_key()
        password_hash = encrypt_password(key, hashed_password.decode())
        cursor.execute('UPDATE users SET password_hash = ? WHERE id = ?', (password_hash, user_id))
        conn.commit()
        conn.close()
        print(f"Password for user ID {user_id} changed successfully.")
        return True
    except Exception as e:
        print(f"An error occurred during password change: {e}")
    finally:
        if conn:
            conn.close()
    return False