from flask import Flask, request
import bcrypt


app = Flask(__name__)

# Define a user class to store user information

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), gensalt())


# Define a dictionary to store user information
users = {}

# Define a route to register a new user
@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the request
    username = request.form['username']
    password  =request.form['password']

    # Check if the username is already taken
    if username in users:
        return "Username already taken"
    

    # Create a new user object and store it in the users dictionary
    users[username] = User(username, password)

    return "User registered successfully"


# Define a route to login a user
@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request
    username =request.form['username']
    password = request.form['password'].encode('utf-8')


    # Check if the username is valid
    if username not in users:
        return "Invalid username or password"
    
    # Verify the password for the given username
    if bcrypt.checkpw(password, users[username].password):
        return "Login successful"
    else:
        return "Invalid username or password"
    
if __name__ == "__main__":
    app.run(debug=True)
