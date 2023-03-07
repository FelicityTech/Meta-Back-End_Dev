import re

#You can use parentheses in regular expressions to 
# group parts of a pattern together and capture 
# the matched substrings as separate groups. 
# You can access the captured groups using the group()
#  method of the match object. The group(0) method returns 
# the entire match, while group(n) returns the substring 
# matched by the n-th group, starting from 1.
pattern = re.compile(r'(\d+) (dollars|euros)')
string = 'I have 10 dollars and 20 euros'
match = pattern.search(string)

print(match.group())

#  the regular expression pattern matches one or more digits 
# followed by either the word "dollars" or "euros", and captures 
# each part as a separate group. The (\d+) syntax creates a group 
# that matches one or more digits, while the (dollars|euros) syntax 
# creates a group that matches either the word "dollars" or "euros". 
# As a result, match.group(1) captures the string "10", and match.group(2) 
# captures the string "dollars"