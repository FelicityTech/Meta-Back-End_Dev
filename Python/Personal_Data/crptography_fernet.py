from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()


# Create a Fernet object using the key
fernet = Fernet(key)


# Encrypt some personal data
personal_data = 'This is my personal data'
encrypted_data = fernet.encrypt(personal_data.encode())


# Decrypt the encrypted data
decrypted_data = fernet.decrypt(encrypted_data)

# Print the decrypted data
print(decrypted_data.decode())