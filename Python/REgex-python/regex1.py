import re

pattern = re.compile(r'hello')

string = 'hello world'
match = pattern.search(string)

print(match.group())
print(match.start())
print(match.end())