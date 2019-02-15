# Solution to 2019 problem 4

# Task
# Write a program that asks the user to input any positive integer and outputs the
# successive values of the following calculation performed on it up to and including
# when the value becomes 1. The calculation is: if the number is even, divide it by
# two, if it is odd then multiply it by three and add one.

# $ python collatz.py
# Please enter a positive integer: 10
# 10 5 16 8 4 2 1

num = input("Please enter any positive integer: ")

while not num.isnumeric() or int(num) < 0 :      # re-used code from solution 1
    num = input("Please enter any positive integer: ")

num = int(num)

while num != 1:
    if num % 2 == 0:
        num /= 2
        print(int(num))
    else :
        num = num * 3 + 1
        print(int(num))
