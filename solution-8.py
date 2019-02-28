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
str1 = dt.datetime.strftime(dt.datetime.now(), '%A, %B ') # Get the day and month and put in str1

# Get date, strip the zero and append the approriate 
str2 = dt.datetime.strftime(dt.datetime.now(), '%d ' )
str2 = str2.replace(' 0','')

# Adapted from https://stackoverflow.com/a/36977549. This works but I dont know how the lambda function works.
#suf = lambda n: "%d%s"%(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10,"th"))
#str2 = suf(int(str2))

# So I did this instead with brute force. Make a list with all the ordinal numbers and assign todays to str2
ordinal = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
str2 = ordinal[int(str2) -1] # assign element at str2 - 1, 

# Adapted from https://stackoverflow.com/a/9526003
str3 = dt.datetime.strftime(dt.datetime.now(), ' %Y at %I:%M%p' ) # str3 is assigned 'Year at HH:MM/AM/PM(in caps)
str3 = str3.replace('PM','pm').replace('AM','am').replace(' 0',' ')  # replace AM/PM with am/pm (as seesm to be the requirement) and strip the leading zero on the hour

print(str1 + str2 + str3) # print the concatanated string