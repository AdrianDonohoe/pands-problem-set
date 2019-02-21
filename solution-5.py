# Created by Adrian Donohoe 15th February 2019
# Solution to 2019 problem 5

# Task

# Write a program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime.
# $ python primes.py
# Please enter a positive integer: 19
# That is a prime.

num = input("Please enter any positive integer: ")

while not num.isnumeric() or int(num) < 0 :      # Adapted code from solution 1, while input is not numeric or not a positive number , keep asking for input
    num = input("Please enter any positive integer: ")

num = int(num)  # make num an integer as input() returns a string

if num == 1 :     # 1 is not prime and logic below can't test that so have added this statement
    print(num, "is not prime")
else:     # else if num is not equal 1 run this block of statements
    # Adapted from python tutorial https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
    for i in range(2,num):  # loop from 2 to the inputted number
        if num % i == 0:    # if num is divisible by any i in range 2 to num 
            print(num , "is not prime") 
            break      # this breaks the innermost for loop. If number is found not to be prime, the for loop is broken and the else won't run
    else :
        print(num , "is prime")
