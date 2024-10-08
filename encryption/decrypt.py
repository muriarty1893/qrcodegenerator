from datetime import datetime, timedelta
from Crypto.Cipher import AES
import base64

key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)

def decrypt_data(encrypted_data):
    encrypted_data = base64.b64decode(encrypted_data)
    nonce = encrypted_data[:16]
    encrypted_message = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt(encrypted_message).decode('utf-8')
    data, timestamp_str = decrypted_data.split('|')
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
    if datetime.now() > timestamp + timedelta(hours=24):
        return "Error: QR Code has expired."
    return data
