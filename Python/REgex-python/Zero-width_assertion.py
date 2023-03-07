import re

"""Zero-width assertions allow you to match a 
pattern only if it is at a certain position in 
the string, without including the position itself 
in the final match. You can use the syntax ^ for a 
start-of-string assertion, $ for an end-of-string assertion,
 \b for a word boundary assertion, and \B for a non-word boundary 
 assertion"""

pattern = re.compile(r'\bcat\b')
string1 = 'The cat is cute'
string2 = 'A catwalk is a type of runway'
match1 = pattern.search(string1)
match2 = pattern.search(string2)

print(match1.group())
# print(match2.group())

# the regular expression pattern matches the string "cat" only if it is surrounded by 
# word boundaries. The \b syntax creates zero-width assertions that match the beginning
# and end of a word.

