import re

pattern = re.compile(r'(\d{3}-\d{4})')

string = 'My phone number is 123-456-7890.'
match = pattern.search(string)
print(match.group())
area_code = match.group(1)
print(area_code)

phone_number = match.group(2)
print(phone_number)