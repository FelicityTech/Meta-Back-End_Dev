import re

pattern = re.compile(r'(?<=\bMr\. )\w+')
string = 'Mr. Smith is a nice guy'
match = pattern.search(string)
name = match.group(0)

print(name)

#The (?<=\bMr\. ) syntax is a positive 
# lookbehind assertion that checks for 
# the presence of the string "Mr. " without 
# including it in the final match.