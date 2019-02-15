# Solution to 2019 problem 1

# Task
# Write a program that takes any positive integer and outputs the sum of all numbers
# between 1 and that number.
# $ python sumupto.py
#  Please enter a positive integer: 10
# 55

# declare variables needed
ans = 0

# Request user to input a postive integer
x = input("Please enter a positive integer: ")


# Check if string is numeric
# got this str.isnumeric() from https://docs.python.org/3/library/stdtypes.html
# got this from https://stackoverflow.com/questions/22377668/python-while-false-loop
#PC was hanging with very large numbers so added the condtion of number not being > 20,000,000
while not x.isnumeric() or int(x) > 20000000 or int(x) < 0 :
    x = input("Please enter a positive integer (less than 20,000,000 as it may crash PC): ") 

# input() returns a string but we need a number 
number = int(x)

# Thyis solution was presented in week 4 video
while number > 0:
    ans += number
    number -= 1
     
# print out the answer 'ans'    
print("Sum of all numbers between 1 and ", x , " is : ", ans)
