import cv2
from pyzbar.pyzbar import decode

def scan_qr_code(image_path):
    img = cv2.imread(image_path)
    detected_qr = decode(img)
    
    for qr in detected_qr:
        encrypted_data = qr.data.decode('utf-8')
        return encrypted_data
    return None
