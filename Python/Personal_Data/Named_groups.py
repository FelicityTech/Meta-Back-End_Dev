import re

# You can assign names to capture groups in 
# regular expressions by using the (?P<name>...) 
# syntax, where name is the name of the group. 
# You can access the captured groups using 
# the groupdict() method of the match object, 
# which returns a dictionary of named capture groups 
# and their matched substrings

pattern = re.compile(r'(?P<amount>\d+) (?P<currency>dollars|euros)')
string = 'I have 10 dollars and 20 euros'
match = pattern.search(string)

print(match.group())

# the regular expression pattern matches one or more digits 
# followed by either the word "dollars" or "euros", and assigns 
# the names "amount" and "currency" to the capture groups. 
# The (?P<amount>\d+) syntax assigns the name "amount" to the group 
# that matches one or more digits, while the (?P<currency>dollars|euros) syntax 
# assigns the name "currency" to the group that matches either the word "dollars" or "euros". 
# As a result, match.groupdict() returns the dictionary {'amount': '10', 'currency': 'dollars'}.