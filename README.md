# QR Code Encryption Project

This project demonstrates how to encrypt data from a CSV file, convert it into a QR code, scan it using a mobile app, and then decrypt the message back into its original form.

## Features

- Encrypt data using AES encryption
- Generate a QR code from the encrypted message
- Scan QR code to retrieve the encrypted message
- Decrypt the encrypted message back to its original form

## Project Structure

```bash
qr_encryption_project/
│
├── encryption/                # Encryption and Decryption logic
│   ├── __init__.py
│   ├── encrypt.py
│   ├── decrypt.py
│
├── data_processing/           # CSV data handling
│   ├── __init__.py
│   ├── csv_handler.py
│
├── qr_code/                   # QR code generation and scanning
│   ├── __init__.py
│   ├── qr_generator.py
│   ├── qr_scanner.py
│
├── main.py                    # Main script to run the project
├── generate_csv.py            # Script to generate sample CSV data
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── data.csv                   # Sample data file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qr_encryption_project.git
   cd qr_encryption_project
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Generate Sample CSV**:  
   Run the script to create a sample CSV file:
   ```bash
   python generate_csv.py
   ```

2. **Run the Main Application**:  
   Execute the main script to read, encrypt, generate QR, scan, and decrypt the message:
   ```bash
   python main.py
   ```

3. **Scan the QR Code**:  
   After the QR code is generated, you can scan it with a mobile app to retrieve the encrypted message.

## License

This project is licensed under the MIT License.
