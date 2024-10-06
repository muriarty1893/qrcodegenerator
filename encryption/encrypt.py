from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted

def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)
