# Solution to 2019 problem 5

# Task

# Write a program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime.
# $ python primes.py
# Please enter a positive integer: 19
# That is a prime.

num = input("Please enter any positive integer: ")

while not num.isnumeric() or int(num) < 0 :      # re-used code from solution 1, check if a positive number
    num = input("Please enter any positive integer: ")

num = int(num)

if num == 1 :     # 1 is not prime and logic below can't test that so have added this statement
    print(num, "is not prime")
else:
    for i in range(2,num):
        if num % i == 0:
            print(num , "is not prime")
            break
    else :
        print(num , "is prime")
