from datetime import datetime
from Crypto.Cipher import AES
import base64

key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)

def encrypt_data(data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data_with_timestamp = f"{data}|{timestamp}"
    nonce = cipher.nonce
    encrypted_data, tag = cipher.encrypt_and_digest(data_with_timestamp.encode('utf-8'))
    return base64.b64encode(nonce + encrypted_data).decode('utf-8')
