import bcrypt
# Hash a user's password before storing it in the database
def hash_password(password):
    # salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode())
    return hashed_password


# Verify a user's password during authentication
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)


# Example usage
password = 'myPassword123'
hashed_password = hash_password(password)
print('Hashed password:', hashed_password)
is_password_valid = verify_password(password, hashed_password)