# Created by Adrian Donohoe 6th March 2019
# Solution to 2019 problem 9

# Task

# Write a program that reads in a text file and outputs every second line.
# The program should take the filename from an argument on the command line.
# $ python second.py moby-dick.txt
# Title: Moby Dick; or The Whale
# CHAPTER 1
# Call me Ishmael. Some years ago--never mind how long
# particular to interest me on shore, I thought I would sail about a

import sys # if we want to pass arguments using argv we must import sys module. Adapted from python tutorial https://docs.python.org/3/tutorial/interpreter.html#argument-passing

with open(sys.argv[1],'r') as f:   # open file as f. covered in week 7 video. Must use argv[1] as the filename is the second argumemt after the python command
    l = list(f)   # create a list from file. Adapted from https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

for i in range(0,len(l),2): # loop over the list in steps of 2.
    print(l[i],end='')   # print, with end ='' to stop the newline