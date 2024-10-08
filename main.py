from qr_code.qr_generator import generate_qr
from qr_code.qr_scanner import scan_qr
from encryption.encrypt import encrypt_data
from encryption.decrypt import decrypt_data
from data_processing.csv_handler import read_csv_data

def main():
    data = read_csv_data('data.csv')
    encrypted_data = encrypt_data(data)
    qr_code_file = 'encrypted_qr.png'
    generate_qr(encrypted_data, qr_code_file)
    print(f"QR Code generated and saved as {qr_code_file}.")
    scanned_data = scan_qr(qr_code_file)
    print(f"Scanned Encrypted Data: {scanned_data}")
    decrypted_data = decrypt_data(scanned_data)
    print(f"Decrypted Data: {decrypted_data}")

if __name__ == "__main__":
    main()
