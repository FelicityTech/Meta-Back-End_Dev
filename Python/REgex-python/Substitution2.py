import re
# You can use regular expressions in Python
#  to replace matched substrings in a string 
# with a new substring using the sub() function. 
# The sub() function takes two arguments: 
# the regular expression pattern to match, 
# and the replacement string. You can use \1, \2, 
# and so on in the replacement string to refer 
# to captured groups in the regular expression pattern.


pattern = re.compile(r'(\d+) (dollars|euros)')
string = 'I have 10 dollars and 20 euros'
new_string = pattern.sub(r'\2 \1', string)

print(new_string)

# the regular expression pattern matches one or more digits followed by either the word "dollars" or "euros", and captures each part as a separate group. The sub() function replaces each matched substring with the second group followed by the first group, effectively swapping the order of the two parts. As a result, new_string is equal to "dollars 10 and euros 20".