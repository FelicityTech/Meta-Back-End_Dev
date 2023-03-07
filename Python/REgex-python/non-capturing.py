import re

# Non-capturing groups allow you to group part of 
# a regular expression together without capturing 
# the matched text. You can use the syntax (?:pattern) 
# to create a non-capturing group.
pattern = re.compile(r'(?:https?://)?example\.com')
string1 = 'http://www.example.com'
string2 = 'www.example.com'
match1 = pattern.search(string1)
match2 = pattern.search(string2)
print(match1.group())
print(match2.group())

# the regular expression pattern matches a URL that may or may not start with 
# "http://" or "https://" and may or may not have "www." in the domain name. 
# The (www\.)? syntax creates a non-capturing group that matches "www." if it 
# is present in the domain name, but does not capture it as a separate group.