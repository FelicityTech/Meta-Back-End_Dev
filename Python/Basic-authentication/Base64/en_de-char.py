import base64
# Encoding and decoding data using custom character sets:


# """By default, the b64encode and b64decode functions 
# use the standard Base64 character set 
# (ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/).
#  However, you can also specify a custom character set to use instead."""

 # Define custom character set
custom_charset = b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-.'

# Encode data custom character set
message = b'Hello, world!'
encoded_message = base64.b64encode(message, custom_charset)
print(encoded_message)

# Decode data using custom character set
decoded_message = base64.b64decode(encoded_message, custom_charset)
print(decoded_message)


# Not working yet