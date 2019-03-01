# Created by Adrian Donohoe 28th February 2019
# Solution to 2019 problem 7

# Task

# Write a program that that takes a positive floating point number as input and outputs
#an approximation of its square root.
# $ python squareroot.py
# Please enter a positive number: 14.5
# The square root of 14.5 is approx. 3.8.

import math as m

num = input("Please enter any positive number: ")

while not num.replace('.','').isnumeric() or float(num) < 0:      # Adapted code from solution 1, while input is not numeric (have to remove the . so floats work) or not a positive number , keep asking for input
    num = input("Please enter any positive number: ")

print(m.sqrt(float(num)))