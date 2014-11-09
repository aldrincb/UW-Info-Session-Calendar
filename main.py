#!/usr/bin/python

# import modules
import urllib2
import re
import dateUtil

def main():

	url = "http://www.ceca.uwaterloo.ca/students/sessions_details.php?id=" 
	url += dateUtil.currentYear() 
	url += dateUtil.currentMonth() 
	string_to_parse = urllib2.urlopen(url).read()
	
	print re.findall ( '45%">(.*?)</td', string_to_parse, re.DOTALL)


if __name__ == '__main__':
    main()


