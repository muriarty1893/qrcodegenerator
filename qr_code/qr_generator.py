import qrcode

def create_qr_code(data, filename='qrcode.png'):
    # Verinin uzunluğuna göre sürümü dinamik ayarlayın
    if len(data) < 50:  # Örnek olarak, 50 karakterden küçükse
        version = 1
    elif len(data) < 150:
        version = 2
    elif len(data) < 300:
        version = 3
    elif len(data) < 600:
        version = 4
    else:
        version = 40  # Maksimum sürüm

    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code saved as {filename}")
