"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#cur_year = datetime.now().year
#cur_month = datetime.now().month

#month_input = int(input("Enter the month ex:4 : ") or cur_month)
#year_input = int(input("Enter the year ex:2020: ") or cur_year)
#print(calendar.month(year_input,month_input))


args = sys.argv
print(len(args))

# start calendar on Sunday:
c = calendar.TextCalendar(calendar.SUNDAY)
# if no value given, default to current date:
month = datetime.now().month
year = datetime.now().year
# if only month is given:
if len(args) == 2:
    month = int(args[1])
# if month and year are given:
elif len(args) == 3:
    month = int(args[1])
    year = int(args[2])
# if something other is given:
else:
    print("ERROR: Should be in format: '14_cal.py [month] [year]'")
# if incorrect month value given:
if month < 1 or month > 12:
    print("ERROR: Invalid entry for month, should be 1-12")
    exit()
c.prmonth(year, month)






