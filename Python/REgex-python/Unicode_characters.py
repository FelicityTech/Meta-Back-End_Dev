import re

# Regular expressions in Python 
# can handle Unicode characters by 
# using the \uXXXX or \UXXXXXXXX syntax 
# to match characters by their Unicode code 
# point. You can also use the \w, \W, \d, \D, \s, 
# and \S shorthand character classes to match Unicode 
# characters that fall within certain categories, such as 
# whitespace or digits
pattern = re.compile(r'\u03A9')
string = 'The Greek letter \u03A9 represents omega'
match = pattern.search(string)

print(match.group())

# In this example, the regular expression pattern matches 
# the Unicode character with code point U+03A9, which represents 
# the Greek letter omega. The \u03A9 syntax is used to specify the Unicode
#  code point in the regular expression pattern. As a result, match captures the 
# string "\u03A9".
