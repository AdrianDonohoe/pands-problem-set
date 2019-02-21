# Created by Adrian Donohoe 8th February 2019
# Solution to 2019 problem 2

# Task
# Write a program that outputs whether or not today is a day that begins with the
# letter T. An example of running this program on a Thursday is as follows.
# $ python begins-with-t.py
# Yes - today begins with a T.

# An example of running it on a Wednesday is as follows.
# $ python begins-with-t.py
# No - today does not begin with a T.

# Adapted from week 2 lecture
import datetime
tday = datetime.datetime.today().weekday() # assign day of the week in number to tday Mon=0, Tues=1 ....

# Create a dictionary of days of the week, Adapted from Python tutorial https://docs.python.org/3/tutorial/datastructures.html#dictionaries
alldays = { 0: 'Monday', 1: 'Tuesday', 2 : 'Wednesday', 3: 'Thursday', 4 : 'Friday', 5 : 'Saturday', 6 : 'Sunday'}

# Create a string s for today by accessing dictionary alldays at key tday
s=alldays[tday]

# Check if first character of the today string begins with a T, then print something and if not, print something else
if s[0] == 'T':
    print('Yes - today begins with a T.')
else:
    print('No - today does not begin with a T.')




