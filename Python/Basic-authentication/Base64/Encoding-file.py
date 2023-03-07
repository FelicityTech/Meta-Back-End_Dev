import  base64

# Open file to encode
with open('file.jpg', 'rb') as file:
    # Encode file contents in Base64
    encoded_data = base64.b64encode(file.read())
    print(encoded_data)