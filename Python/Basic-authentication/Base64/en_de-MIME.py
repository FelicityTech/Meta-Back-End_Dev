import base64

"""Base64 encoding is commonly used in MIME 
(Multipurpose Internet Mail Extensions) format, 
which is used for sending emails with attachments. 
The base64 module provides a encodebytes function that
 can be used to encode data in MIME format."""

 # Encode data in MIME format
message = b'Hello, world!'
encoded_message = base64.encodebytes(message)
print(encoded_message)


# Decode data from MIME format
decoded_message = base64.decodebytes(encoded_message)
print(decoded_message)