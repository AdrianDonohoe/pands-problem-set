# Solution to 2019 problem 3

# Task
# Write a program that prints all numbers between 1,000 and 10,000 that are divisible
# by 6 but not 12.

# $ python divisors.py
# 1002
# 1014
# 1026
# etc
# 9990

for i in range(1000,10001):     # loop over range 1000 -> 10000
    if i % 6 == 0 and i % 12 != 0 :      # if divisble by 6 and not divisible by 12, then print
        print(i)

