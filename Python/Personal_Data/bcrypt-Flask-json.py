from flask import Flask, jsonify, request
import bcrypt


app = Flask(__name__)

# Define a function to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    password = request.json['password']

    # Hash the password using a radom salt
    hash_password = bcrypt.hashpw(password.encode('utf=8'), bcrypt.gensalt())

    # Create a new user object and save it to the database
    # (in this example, we're just storing users in memory)
    user = {
        'username': username,
        'password': hash_password
    }

    users.append(user)

    return jsonify({'message':'User created successfully'})


# Define a function to authenticate a user'
@app.route('/login', methods=['POST'])
def authenticate_user():
    username = request.json['username']
    password = request.json['password']

    try:
        # Get the user object from the database
        user = next((u for u in users if u['username'] == username))

        # Verify the password using the bcrypt package
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return jsonify({'message': 'Authentication successful'})
    except StopIteration:
        pass

    return jsonify({'message': 'Authentication failed'})


if __name__ == '__main__':
    # In this example, we're just storing users in memory
    users = []


    app.run()

    

