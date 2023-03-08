import getpass

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")


if username == 'myusername' and password == 'mypassword':
    print("Authentication successful")
else:
    print("Authentication failed")

    # his code prompts the user to enter their username and 
    # password, and then checks whether the credentials match 
    # the expected values (in this case, "myusername" and "mypassword").
    # The getpass.getpass function is used to securely prompt the user 
    # for their password without displaying it on the screen.