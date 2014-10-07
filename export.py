import urllib2
import re

# the year and month are hard coded for testing
string_to_parse = urllib2.urlopen("http://www.ceca.uwaterloo.ca/students/sessions_details.php?id=2014Oct").read()

regex = re.compile("\">(.*)</")
r = regex.search(string_to_parse)
r
regex.match(string_to_parse)
r.groups()
r.groupdict()
print regex.findall(string_to_parse)