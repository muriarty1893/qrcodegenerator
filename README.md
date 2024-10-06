# QR Code Encryption Project

This project encrypts data from a CSV file, generates a QR code with the encrypted data, and then allows the encrypted message to be scanned and decrypted via a mobile QR code scanner. The project ensures that the decrypted message is displayed in plain text after being inputted into the application.

## Features

- Read data from a CSV file
- Encrypt the data using a symmetric encryption algorithm (AES)
- Generate a QR code with the encrypted data
- Scan the QR code with a mobile app to retrieve the encrypted message
- Decrypt the message using the app to reveal the original plain text

## Dependencies

To run this project, you need the following Python packages installed:

- `cryptography` (for AES encryption)
- `qrcode` (for generating QR codes)
- `pandas` (for handling CSV files)
- `opencv-python` or `zbarlight` (for scanning QR codes)

You can install the required packages using pip:


pip install cryptography qrcode[pil] pandas opencv-python
How to Run the Project
Generate CSV Data: If you don't have a CSV file, generate one as shown below:

python generate_csv.py
The file data.csv will be created with sample data.

Encrypt Data and Generate QR Code:

Use the provided script to read the CSV file, encrypt the data, and create a QR code with the encrypted content.

python encrypt_to_qr.py data.csv
This will output a QR code image file, which you can scan using a mobile QR code scanner.

Decrypt Data:

After scanning the QR code and retrieving the encrypted message, input the encrypted text into the app to decrypt the message:


Kodu kopyala
python decrypt_message.py
You will be prompted to enter the encrypted message. After decryption, the original data will be displayed.

File Structure
generate_csv.py: Generates the data.csv file with sample data.
encrypt_to_qr.py: Reads the CSV file, encrypts the data, and generates a QR code.
decrypt_message.py: Prompts the user to enter the encrypted message, decrypts it, and displays the original data.
README.md: This file, providing information on how to use the project.
Example

Original CSV File:

ID,Name,Age,Email<br>
1,Alice,25,alice@example.com<br>
2,Bob,30,bob@example.com<br>
Encrypted QR Code: After running the encrypt_to_qr.py script, a QR code image will be generated with the encrypted content of the CSV.

Decryption: Once the QR code is scanned, the encrypted message can be decrypted back to its original form using the decryption script.

Future Improvements
Implement a web interface for the encryption and decryption process.
Add more sophisticated encryption methods.
Improve error handling for incorrect inputs.

License
This project is licensed under the MIT License - see the LICENSE file for details.


Bu içeriği GitHub projenizdeki `README.md` dosyasına yapıştırarak direkt kullanabilirsiniz. 
