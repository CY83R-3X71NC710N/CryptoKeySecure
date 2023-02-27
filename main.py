
#!/usr/bin/env python
# CY83R-3X71NC710N Copyright 2023

# Import Statements
import os
import sys
import time
import random
import string
import cryptography
import matplotlib
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Main Code
def generate_key():
    """Generates a random key for encryption/decryption"""
    key = Fernet.generate_key()
    return key

def encrypt_file(file_name, key):
    """Encrypts a file using the given key"""
    f = Fernet(key)
    with open(file_name, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_name, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_name, key):
    """Decrypts a file using the given key"""
    f = Fernet(key)
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_name, 'wb') as file:
        file.write(decrypted_data)

def generate_password(length):
    """Generates a random password of the given length"""
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for i in range(length))
    return password

def generate_salt():
    """Generates a random salt for use in encryption/decryption"""
    salt = os.urandom(16)
    return salt

def generate_key_from_password(password, salt):
    """Generates a key from a given password and salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

# GUI Development
def main():
    """Main function for the program"""
    print("CryptoKeySecure")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Generate Password")
    print("4. Generate Salt")
    print("5. Generate Key from Password")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        file_name = input("Enter the file name: ")
        key = generate_key()
        encrypt_file(file_name, key)
        print("File encrypted successfully!")
    elif choice == '2':
        file_name = input("Enter the file name: ")
        key = input("Enter the key: ")
        decrypt_file(file_name, key)
        print("File decrypted successfully!")
    elif choice == '3':
        length = int(input("Enter the password length: "))
        password = generate_password(length)
        print("Generated password:", password)
    elif choice == '4':
        salt = generate_salt()
        print("Generated salt:", salt)
    elif choice == '5':
        password = input("Enter the password: ")
        salt = input("Enter the salt: ")
        key = generate_key_from_password(password, salt)
        print("Generated key:", key)
    elif choice == '6':
        sys.exit()
    else:
        print("Invalid choice!")
    main()

if __name__ == '__main__':
    main()
