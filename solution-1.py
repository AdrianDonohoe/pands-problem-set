# Created by Adrian Donohoe 7th February 2019
# Solution to 2019 problem 1

# Task
# Write a program that takes any positive integer and outputs the sum of all numbers
# between 1 and that number.
# $ python sumupto.py
#  Please enter a positive integer: 10
# 55

# declare ans variable. This is the final answer to the problem
ans = 0

# Request user to input a postive integer
x = input("Please enter a positive integer: ")


# Check if string is numeric
# Adapted str.isnumeric() from https://docs.python.org/3/library/stdtypes.html
# Use of not adapted from https://stackoverflow.com/a/22377834
# PC was hanging with very large numbers so added the condtion of while number not being > 20,000,000 or not being negative, we will keep asking to input
while not x.isnumeric() or int(x) > 20000000 or int(x) < 0 :
    x = input("Please enter a positive integer (less than 20,000,000 as it may crash PC): ") 

# input() returns a string but we need a number 
number = int(x)

# Adapted from solution presented in week 4 video
while number > 0:   # run the following code until number equals zero
    ans += number   # ans is assigned current value + number  , equivalent to ans = ans + number
    number -= 1     # decrement number and return to top of loop, equivalenet to number = number - 1
     
# When while looo finishes, we print out the answer 'ans'    
print("Sum of all numbers between 1 and ", x , " is : ", ans)
