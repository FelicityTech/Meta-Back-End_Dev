import getpass

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")


if username == 'myusername' and password == 'mypassword':
    print("Authentication successful")
else:
    print("Authentication failed")