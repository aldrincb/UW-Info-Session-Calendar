# returns the month in format XXX
# example: Nov
def currentMonth():
	from datetime import date
	if date.today().month == 1:
		return "Jan"
	if date.today().month == 2:
		return "Feb"
	if date.today().month == 3:
		return "Mar"
	if date.today().month == 4:
		return "Apr"
	if date.today().month == 5:
		return "May"
	if date.today().month == 6:
		return "Jun"
	if date.today().month == 7:
		return "Jul"
	if date.today().month == 8:
		return "Aug"
	if date.today().month == 9:
		return "Sep"
	if date.today().month == 10:
		return "Oct"
	if date.today().month == 11:
		return "Nov"
	if date.today().month == 12:
		return "Dec"

# returns the year in format ####
# example: 1980
def currentYear():
	from datetime import date
	return str(date.today().year)



