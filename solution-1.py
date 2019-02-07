# Solution to 2019 problem 1

# Task
# Write a program that takes any positive integer and outputs the sum of all numbers
# between 1 and that number.
# $ python sumupto.py
#  Please enter a positive integer: 10
# 55

# declare variables needed
number = 0
ans = 0

# Request user to input a postive integer
# learned this from https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments
# input reads in as a string so the int() function is necessary
number = int(input("Please enter a positive integer: "))

# Need to change this to a while loop
if  (number > 20000000) or (number < 0) :
    number = int(input("Please enter a positive number less than 20,000,000 (PC may crash with big numbers) : "))



    print("You entered ", number )


    
#make a list and extend backwards from number to 1 
    l = [number]
    l.extend(range(number - 1, 0, -1))

    for i in range(0, len(l)):
        ans += l[i]
    
    print("Sum of all numbers between 1 and ", number , " is : ", ans)


