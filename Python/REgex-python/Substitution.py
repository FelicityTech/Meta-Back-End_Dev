import re
pattern = re.compile(r'cat')
string = 'The quick brown for catches a cat'
result = pattern.sub('dog', string)

print(result)

# The sub() method takes two arguments: 
# a regular expression pattern and a replacement string

#the regular expression pattern matches the string "cat", 
# and the sub() method replaces it with the string "dog".
# The resulting string is "The quick brown fox catches a dog"

