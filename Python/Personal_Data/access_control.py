class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin


    def can_access_data(self, data):
        if self.is_admin:
            return True
        
        else:
            return self.username == data['owner']
        
    
class DataStore:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self, user):
        return [d for d in self.data if user.can_access_data(d)]
    


# Create some sample data

data_store = DataStore()
data_store.add_data({'owner': 'alice', 'data':'Some personal data'})
data_store.add_data({'owner': 'bob', 'data': 'Some more personal data'})



# Create access control
users = [User('alice', 'password'), User('bob', 'password'), User('admin', 'password', True)]


# Test access control
for user in users:
    print(user.username, 'can access:')
    for d in data_store.get_data(user):
        print(d['data'])
    print()