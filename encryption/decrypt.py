from cryptography.fernet import Fernet

def load_key(filename='secret.key'):
    with open(filename, 'rb') as key_file:
        key = key_file.read()
    return key

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data).decode()
    return decrypted
