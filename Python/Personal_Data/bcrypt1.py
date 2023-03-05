#import the bcrypt module
import bcrypt

#Generate a hashed password
#  using the bcrypt.hashpw() function

password = b"mysecretpassword"
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)


# The gensalt() function generates a random salt value 
# that is used in the hash function to make each password
#  hash unique. The resulting hashed_password is a byte 
# string that can be stored in a database or file.

# Verify a password using the 'bcrypt.checkpw()' function:

input_password = b"mysecretpassword"
if bcrypt.checkpw(input_password, hashed_password):
    print("Password matches")
else:
    print("Invalid password")

    