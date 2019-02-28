# Created by Adrian Donohoe 27th February 2019
# Solution to 2019 problem 8

# Task

# Write a program that outputs today’s date and time in the format ”Monday, January
# 10th 2019 at 1:15pm”.
# $ python datetime.py
# Monday, January 10th 2019 at 1:15pm




# Adapted from week 6 lesson
import datetime as dt

# Will make 3 separate strings then concatanate and print at the end.
str1 = dt.datetime.strftime(dt.datetime.now(), '%A, %B ') # Get the day and month and put in string

# Get date, strip the zero and append the approriate 
str2 = dt.datetime.strftime(dt.datetime.now(), '%d ' )
str2 = str2.replace(' 0','')


# Adapted from https://stackoverflow.com/a/9526003
str3 = dt.datetime.strftime(dt.datetime.now(), ' %Y at %I:%M%p' )
str3 = str3.replace('PM','pm').replace('AM','am').replace(' 0',' ')

# Adapted from https://stackoverflow.com/a/36977549. This works but I dont know how the lambda function works.
suf = lambda n: "%d%s"%(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10,"th"))
str2 = suf(int(str2))


print(str1 + str2 + str3)