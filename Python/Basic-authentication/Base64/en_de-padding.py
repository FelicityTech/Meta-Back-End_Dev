import base64

# Encode data with padding
message = b'Hello world!'
encoded_message = base64.b64encode(message)
print(encoded_message)


# Decode data with padding
decode_message = base64.b64decode(encoded_message)
print(decode_message)


# Encode data without padding
message = b'Hello, world!'
encoded_message = base64.urlsafe_b64encode(message).rstrip(b'=')
print(encoded_message)

# Decode data without padding
decoded_message = base64.urlsafe_b64decode(encoded_message + b'==')
print(decode_message)