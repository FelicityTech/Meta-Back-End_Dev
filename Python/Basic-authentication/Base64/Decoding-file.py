import base64

# Base64-encoded string
encoded_data = b'Rmlyc3QgYXJlIHlvdXIgbWVzc2FnZQ=='


# Decode string
decoded_data = base64.b64decode(encoded_data)

# Write decoded data to file
with open('message.txt', 'wb') as file:
    file.write(decoded_data)