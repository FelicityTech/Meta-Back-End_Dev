import re

pattern = re.compile(r'(\w+) and \1')
string = 'apple and apples'
match = pattern.search(string)

print(match.group(1))