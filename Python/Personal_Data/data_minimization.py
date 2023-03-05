class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_profile(self):
        return {'username': self.username, 'email': self.email}
    


class DataStore:
    def __init__(self):
        self.data = []


    def add_data(self, data):
        self.data.append(data)


    def get_data(self):
        return [d.get_profile() for d in self.data]
    

# Create some sample data

data_store = DataStore()
data_store.add_data(User('alice', 'alice@example.com'))
data_store.add_data(User('bob', 'bob@example.com'))

# Print the user profiles
for profile in data_store.get_data():
    print(profile)