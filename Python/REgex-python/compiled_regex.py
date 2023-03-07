import re


# If you need to perform the same regular expression matching
# operation many times in your code, you can improve performance
# by compiling the regular expression pattern once and reusing it in 
# multiple calls to the search() function. You can use the re.compile() 
# function to compile a regular expression pattern into a compiled regular 
# expression object
pattern = re.compile(r'\d+')
string = 'I have 10 apples and 20 oranges'
matches = pattern.findall(string)

print(matches)


#  the regular expression pattern matches one or more digits in the input string. The re.compile() 
# function is used to compile the pattern into a compiled regular expression object pattern.
# The pattern.findall() function is used to find all occurrences of the pattern in the input string string. 
# As a result, matches is equal to ['10', '20'].