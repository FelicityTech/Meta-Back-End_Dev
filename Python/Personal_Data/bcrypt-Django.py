import bcrypt

# Define a function to create a new user
def create_user(username, password):
    # Hash the password using a random salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


    # Create a new user object and save it to the database
    user = User.objects.create_user(username=username, password=hashed_password.decode('utf-8'))
    user.save()



# Define a function to authenticate a user
def authentication_user(username, password):
    try:
        # Get the user object from database
        user = User.objects.get(username=username)


        # Verify the passwprd using the bcrypt package
        if bcrypt.checkpw(password.encode('utf-8'), use.password.encode('utf-8')):
            return user
    except User.DoesNotExist:
        pass

    return None