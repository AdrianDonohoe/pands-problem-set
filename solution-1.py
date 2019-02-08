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
# learned this from https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments
x = input("Please enter a positive integer: ")


# Check if string is numeric
# got this str.isnumeric() from https://docs.python.org/3/library/stdtypes.html
# got this from https://stackoverflow.com/questions/22377668/python-while-false-loop
while not x.isnumeric():
    x = input("Please enter a positive integer, not a string: ") 



# This while loop checks if the number is postivie and less than 20000001, so my PC doesn't crash
# input reads in as a string so the int() function is necessary
while  (int(x) > 20000000) or (int(x) < 0) :
    x = input("Please enter a positive number less than 20,000,000 (PC may crash with big numbers) : ")

# input() returns a string but we need a number 
number = int(x)
    
# make a list and extend backwards from 'number' to 1 
l = [number]
l.extend(range(number - 1, 0, -1))

# loop over the list and add to number
for i in range(0, len(l)):
    ans += l[i]
    
# print out the answer 'ans'    
print("Sum of all numbers between 1 and ", number , " is : ", ans)
