import re

pattern = re.compile(r'(?<=\$)\d+\.\d{2}(?=\b)')
"""The (?<=\$) and (?=\b) are lookbehind and lookahead assertions, respectively,
 that make sure the dollar sign and word boundary are present without 
 including them in the final match."""

string = 'The price is $9.99.'
match = pattern.search(string)
price = match.group(0)
print(price)