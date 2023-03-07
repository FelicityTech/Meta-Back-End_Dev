import re

pattern = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')
string = 'The date is 2022-03-06.'
match = pattern.search(string)
year = match.group('year')
month = match.group('month')
day = match.group('day')

print(day + '-' + month + '-' +  year)