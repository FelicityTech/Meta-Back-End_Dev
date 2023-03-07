import base64

# Base64 is not a secure method for password 
# hashing, as it is easily reversible. However, 
# it can be used for simple obfuscation of passwords.
# Here is an example of how to hash a password using 
# Base64

password = 'secret'
encoded_password = base64.b64encode(password.encode('utf-8'))

print(encoded_password)

# Note that this is not a secure way to store 
# passwords, and it is recommended to use a proper password 
# hashing algorithm such as bcrypt or Argon2.