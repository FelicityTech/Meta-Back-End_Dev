import base64

# Encode data in URL-safe Base64
message = b'Hello, world!'
encoded_message = base64.urlsafe_b64encode(message)
print(encoded_message)


# Decode data from URL-safe Base64
decoded_message = base64.urlsafe_b64decode(encoded_message)
print(decoded_message)