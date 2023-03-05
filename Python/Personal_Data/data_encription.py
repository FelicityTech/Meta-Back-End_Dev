import hashlib
from Crypto.Cipher import AES


class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = hashlib.sha256(password.encode()).digest()


    def get_data(self):
        return {'username': self.username, 'password_hash': self.password_hash}
    


class DataStore:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
        self.data = []

    def add_data(self, data):
        iv = b'0123456789abcdef'
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_data = []
        for d in self.data:
            decrypted_data.append(cipher.decrypt(d).decode())
        return decrypted_data


# Create some sample data
data_store = DataStore('secret key')
data_store.add_data(User('alice', 'password').get_data())
data_store.add_data(User('Bob', 'password').get_data())

#Retrieve the data using a user with the correct password

user = User('alice', 'password')
print(data_store.get_data(user))


# Try to retrieve the data using a user with the incorrect password
user = User('Bob', 'wrong password')
print(data_store.get_data(user))