# Created by Adrian Donohoe 6th March 2019
# Solution to 2019 problem 9

# Task

# Write a program that reads in a text file and outputs every second line.

with open('numbers.txt','r') as f:   # open file as f. covered in week 7 video.
    l = list(f)   # create a list from file. Adapted from https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

for i in range(0,len(l),2): # loop over the list in steps of 2.
    print(l[i],end='')   # print, with end ='' to stop the newline