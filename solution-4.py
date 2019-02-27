# Created by Adrian Donohoe 15th February 2019
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

while not num.isnumeric() or int(num) < 0 :      # Adapted code from solution 1, while input is not numeric or not a positive number , keep asking for input
    num = input("Please enter any positive integer: ")

num = int(num)  # make num an integer as input() returns a string
print(num, end=' ')  # added end so that prints on same line

while num != 1:   # while num is not equal to one
    if num % 2 == 0:     # if num is even
        num /= 2      # num is assigned num divided by 2, equivalent to num = num / 2
        print(int(num), end=' ')  # for some reason floats were getting printed
    else :    # else ifnum is odd 
        num = num * 3 + 1  # num is assigned num multiplied by 3 and add 1, then print
        print(int(num), end=' ')  # for some reason floats were getting printed
