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

# TBD
#  Test is positive, test is string and ask again if doesn't fit criteria
print("You entered ", number )

# TBD
# Do the arithmetic

#make a list and extend to from number to 1 
l = [number]
l.extend(range(number - 1, 0, -1))

for i in range(0, len(l)):
    ans += l[i]
    
print("Sum of all numbers between 1 and ", number , " is : ", ans)

    


#print("The sum of all numbers between 1 and ", number , "is :")

#print(ans)
