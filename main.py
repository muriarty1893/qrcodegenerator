from encryption.encrypt import generate_key, encrypt_data, save_key
from encryption.decrypt import load_key, decrypt_data
from data_processing.csv_handler import read_csv
from qr_code.qr_generator import create_qr_code
from qr_code.qr_scanner import scan_qr_code

def main():
    # 1. Read data from CSV
    csv_data = read_csv('data.csv')
    print(f"CSV Data:\n{csv_data}")
    
    # 2. Generate encryption key
    key = generate_key()
    save_key(key)
    
    # 3. Encrypt the CSV data
    encrypted_data = encrypt_data(csv_data, key)
    print(f"Encrypted Data: {encrypted_data}")
    
    # 4. Create QR code from encrypted data
    create_qr_code(encrypted_data.decode(), 'qrcode.png')
    
    # 5. Scan QR code and retrieve encrypted message
    scanned_data = scan_qr_code('qrcode.png')
    print(f"Scanned Encrypted Data: {scanned_data}")
    
    # 6. Decrypt the scanned data
    key = load_key()  # Load the encryption key
    decrypted_data = decrypt_data(scanned_data.encode(), key)
    print(f"Decrypted Data:\n{decrypted_data}")

if __name__ == "__main__":
    main()
