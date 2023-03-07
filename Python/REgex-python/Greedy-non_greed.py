import re

# By default, regular expression patterns in Python 
# use greedy matching, which means that they try to match 
# as much of the input string as possible while still satisfying
#  the pattern. However, you can use the ? modifier to make the matching 
# non-greedy, which means that it matches as little of the input string as 
# possible

pattern = re.compile(r'<.*>')
string = '<a> <b> <c>'
match = pattern.search(string)

print(match.group())


# the regular expression pattern matches any sequence of characters enclosed in 
# angle brackets. However, because the pattern uses greedy matching, it matches 
# the entire string " <a> <b> <c>" as a single match, rather than matching each 
# substring separately. To make the matching non-greedy, you can add the ? modifier
#  after the * symbol, like this:

pattern = re.compile(r'<.*?>')
string = '<a> <b> <c>'
match = pattern.search(string)

print(match.group())

# the .*? syntax matches any sequence of characters enclosed in angle brackets, 
# but matches as little of the input string as possible. As a result, match captures 
# the string "<a>".