import re
# Lookahead and lookbehind assertions are zero-width
#  assertions that allow you to match a pattern only
#  if it is followed or preceded by another pattern, 
# without including the lookahead or lookbehind pattern
#  in the match result. Lookahead assertions are denoted 
# by (?=...), while lookbehind assertions are denoted 
# by (?<=...) or (?<!...).

pattern = re.compile(r'\d+(?= dollars)')
string = 'I have 10 dollars and 20 euros'
match = pattern.search(string)

print(match.group()) 

# the regular expression pattern matches one or more digits
# followed by the word "dollars", but does not include "dollars" 
# in the match result. The (?= dollars) syntax is a positive lookahead 
# assertion that matches the pattern " dollars" immediately after the digits.
#  As a result, match captures the string "10".