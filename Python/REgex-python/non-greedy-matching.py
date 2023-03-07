import re

"""By default, regular expressions use greedy matching,
which means they try to match as much of the input string
as possible. You can use the ? modifier to make a quantifier
non-greedy, which means it tries to match as little of the input
 string as possible"""


pattern = re.compile(r'<.*>')
string1 = '<p>hello</p><p>world</p>'
string2 = '<p>hello</p>'
match1 = pattern.search(string1)
match2 = pattern.search(string2)
print(match1.group())
print(match2.group())

# the regular expression pattern matches any string that starts with 
# < and ends with >, including any characters in between. The .* 
# syntax is a greedy quantifier that matches as much of the input string as 
# possible. As a result, match1 captures the entire input string, including 
# both <p> tags. To make the quantifier non-greedy, you can use .*? instead.
