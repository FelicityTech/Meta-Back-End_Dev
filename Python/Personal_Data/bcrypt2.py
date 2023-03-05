import bcrypt

# Hash a password with a random salt
password = b"my_password"
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)
print(hashed_password)


# Verify a password against a hashed password

input_password = b"my_password"
if bcrypt.checkpw(input_password, hashed_password):
    print("Password is correct")
else:
    print("Password is incorrect")