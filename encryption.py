from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def generate_and_store_key():
    """
    Generates a new encryption key and saves it to a file.
    """
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    """
    Loads the encryption key from the file.
    If the file does not exist, it generates and stores a new key.
    """
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
        return key
    else:
        return generate_and_store_key()

def encrypt_password(key, password):
    """
    Encrypts the given password using the provided key.
    """
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(key, encrypted_password):
    """
    Decrypts the given encrypted password using the provided key.
    """
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password