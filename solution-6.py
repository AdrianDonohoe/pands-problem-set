# Created by Adrian Donohoe 27th February 2019
# Solution to 2019 problem 6

# Task

# Write a program that takes a user input string and outputs every second word.
# $ python secondstring.py
# Please enter a sentence: The quick brown fox jumps over the lazy dog.
# The brown jumps the dog

# Request user to input a string, split it and assign to list 
s1 = input("Please enter a sentence: ")

# split string into list  , adapted from https://docs.python.org/3/library/stdtypes.html?highlight=str%20split#str.split
l = s1.split()

for i in range(len(l)):  # loop over the list and print
    print(l[i], end=' ')
