import re

string = 'hello world'
new_string = re.sub(r'hello', 'hi', string)
print(new_string)