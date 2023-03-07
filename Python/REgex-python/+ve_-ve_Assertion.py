import re

pattern = re.compile(r'\w+(?=!)')
string = 'Stop! there'
match = pattern.search(string)
word = match.group(0)

print(word)