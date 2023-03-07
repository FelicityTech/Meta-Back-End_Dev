import base64
# The base64 module can also be used to encode 
# and decode images in various formats such as 
# JPEG, PNG, and GIF. Here is an example of how 
# to encode an image file to Base64 format:

with open("image.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())


print(encoded_string)

# To decode the Base64 string back to an image

with open("image.jpg", "wb") as image_file:
    decoded_string = base64.b64decode(encoded_string)
    image_file.write(decoded_string)