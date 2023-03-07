import base64

# Encode data in Base64
message = b'Hello, world!'
encoded_message = base64.b64encode(message)
print(encoded_message)

""" we first encode a message using the b64encode 
function from the base64 module. This returns a byte
 string containing the Base64-encoded message."""

# Decode data from Base64
decoded_message = base64.b64decode(encoded_message)

print(decoded_message)

"""then decode the Base64-encoded message using the 
b64decode function from the base64 module. 
This returns the original message as a byte string."""

#then decode the Base64-encoded message using the b64decode
#  function from the base64 module. This returns the original 
# message as a byte string.
