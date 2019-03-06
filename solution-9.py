# Created by Adrian Donohoe 6th March 2019
# Solution to 2019 problem 9

# Task

# Write a program that reads in a text file and outputs every second line.

with open('numbers.txt','r') as f:
    l = list(f)

for i in range(0,len(l),2):
    print(l[i],end='')