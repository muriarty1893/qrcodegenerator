import pandas as pd
from cryptography.fernet import Fernet
import qrcode
import cv2
from pyzbar.pyzbar import decode

# 1. CSV dosyasını okuma ve veriyi işleme
def read_csv(file_path):
    # CSV dosyasını okuma
    data = pd.read_csv(file_path)
    # CSV dosyasındaki ilk satırı alıyoruz (örneğin, bir kimlik numarası olabilir)
    return data.iloc[0].to_string(index=False)  # Veriyi string formatına dönüştürüyoruz

# 2. Şifreleme işlemi
def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())  # Veriyi şifreliyoruz
    return encrypted_data

# 3. QR kod oluşturma
def create_qr_code(data, qr_file_path):
    qr = qrcode.QRCode(
        version=1,  # QR kodun karmaşıklığı
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
        box_size=10,  # QR kod kutu boyutu
        border=4,  # QR kod sınırı
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(qr_file_path)  # QR kodu dosya olarak kaydediyoruz
    print(f"QR kod kaydedildi: {qr_file_path}")

# 4. QR kodu çözme
def decode_qr_code(qr_file_path):
    img = cv2.imread(qr_file_path)  # QR kodu okuma
    decoded_objects = decode(img)
    if decoded_objects:
        decoded_data = decoded_objects[0].data.decode()  # Şifreli veriyi alıyoruz
        return decoded_data
    else:
        print("QR kod çözülemedi!")
        return None

# 5. Şifreyi çözme işlemi
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data.encode())  # Şifreyi çözüyoruz
    return decrypted_data.decode()

# Ana fonksiyon
if __name__ == "__main__":
    # 6. Önce bir anahtar oluşturma (Bu anahtar her iki işlemde de kullanılmalı)
    key = Fernet.generate_key()  # Anahtar oluşturma
    print(f"Anahtar: {key.decode()}")  # Şifreleme ve şifre çözme işlemi için kullanılan anahtar

    # 7. CSV dosyasından veri alma
    file_path = "data.csv"  # CSV dosyanızın yolu
    data = read_csv(file_path)
    print(f"Okunan veri: {data}")

    # 8. Veriyi şifreleme
    encrypted_data = encrypt_data(data, key)
    print(f"Şifrelenmiş veri: {encrypted_data}")

    # 9. Şifrelenmiş veriyi QR koda çevirme
    qr_file_path = "encrypted_qr.png"
    create_qr_code(encrypted_data, qr_file_path)

    # QR kodu okuma ve çözme (örneğin, uygulamada bir QR kodu okutmuş olacağız)
    decoded_message = decode_qr_code(qr_file_path)
    if decoded_message:
        print(f"QR koddan okunan şifreli mesaj: {decoded_message}")

        # 10. QR koddan okunan mesajı (şifreli hali) çözme
        decrypted_data = decrypt_data(decoded_message, key)
        print(f"Şifre çözülmüş veri: {decrypted_data}")
