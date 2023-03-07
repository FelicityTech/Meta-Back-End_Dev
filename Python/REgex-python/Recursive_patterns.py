import re

# Recursive patterns are regular expression patterns that contain references to themselves, allowing them
#  to match nested structures like nested parentheses, HTML tags, or JSON objects. In Python, you can use 
# the (?P>name) syntax to refer to a named capture group within the same regular expression pattern
pattern = re.compile(r'<(?P<tag>[a-z]+)(?P<attrs>(?:\s+[a-z]+\s*=\s*"[^"]*")*))\s*(?P<content>/)?>')
string = '<div class="foo" id="bar">content</div>'
match = pattern.search(string)

print(match.group())

# the regular expression pattern matches an HTML tag with optional attributes and content. The (?P<tag>[a-z]+) 
# syntax matches the tag name, the (?P<attrs>(?:\s+[a-z]+\s*=\s*"[^"]*")*)) syntax matches any number of attributes,
# and the (?P<content>/)?> syntax matches an optional closing slash and angle bracket. Note that the 
# (?P<attrs>(?:\s+[a-z]+\s*=\s*"[^"]*")*) syntax uses a non-capturing group (?:...) to allow for multiple attributes 
# to be matched recursively. As a result, match.groupdict() returns the dictionary 
# {'tag': 'div', 'attrs': ' class="foo" id="bar"', 'content': 'content'}.