# Created by Adrian Donohoe 27th February 2019
# Solution to 2019 problem 6

# Task

# Write a program that takes a user input string and outputs every second word.
# $ python secondstring.py
# Please enter a sentence: The quick brown fox jumps over the lazy dog.
# The brown jumps the dog

# Request user to input a string, split it and assign to list 
s1 = input("Please enter a sentence: ")

# adapted from https://stackoverflow.com/a/3559600
s1 = s1.replace(',','') # remove comma's
s1 = s1.replace('.','') # remove full stops

# split string into list, adapted from https://docs.python.org/3/library/stdtypes.html?highlight=str%20split#str.split
l = s1.split()

for i in range(0,len(l),2):  # loop from start to length of list in steps of 2 
    print(l[i], end=' ')     # and print list element i with space 
