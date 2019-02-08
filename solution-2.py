# Solution to 2019 problem 2

# Task
# Write a program that outputs whether or not today is a day that begins with the
# letter T. An example of running this program on a Thursday is as follows.
# $ python begins-with-t.py
# Yes - today begins with a T.

# An example of running it on a Wednesday is as follows.
# $ python begins-with-t.py
# No - today does not begin with a T.

# we learned this in an earlier example
import datetime

# assign day of the week in number to tday Mon=0, Tues=1 ....
tday = datetime.datetime.today().weekday()

# print(tday)

# Create a dictionary of days of the week
alldays = { 0: 'Monday', 1: 'Tuesday', 2 : 'Wednesday', 3: 'Thursday', 4 : 'Friday', 5 : 'Saturday', 6 : 'Sunday'}





