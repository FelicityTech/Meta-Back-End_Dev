import re
pattern = re.compile(r'this is a test', re.IGNORECASE)
string = 'THIS IS A TEST'
match = pattern.search(string)

print(match.group())

#Flags allow you to modify the behavior of a regular expression.
# You can use flags by passing them as a second argument to 
# the re.compile() function

#  the regular expression pattern matches the string "this is a test" case-insensitively.
# The re.IGNORECASE flag is passed as a second argument to the re.compile() function to 
# enable case-insensitive matching

