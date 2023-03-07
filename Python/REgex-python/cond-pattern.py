import re
pattern = re.compile(r'(?(?=.*\d)\d+|[a-zA-Z]+)')
string = '12345'
match = pattern.search(string)
result = match.group(0)

print(result) # not working yet