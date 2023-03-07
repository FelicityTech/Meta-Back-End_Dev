import re

# You can pass compilation flags to the re.compile() 
# function in Python to modify the behavior of regular 
# expression patterns. For example, you can use the 
# re.IGNORECASE flag to make the pattern case-insensitive,
#  or the re.DOTALL flag to make the dot character match newline 
# characters as well. You can combine multiple flags using the | symbol.

pattern = re.compile(r'hello. *world', re.IGNORECASE | re.DOTALL)
string = 'Hello\nWorld'
match = pattern.search(string)

# In this example, the regular expression pattern matches any sequence 
# of characters that starts with the string "hello" and ends with 
# the string "world", ignoring case and matching newline characters as well. 
# As a result, match captures the string "Hello\nWorld".

