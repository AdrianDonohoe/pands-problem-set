# Created by Adrian Donohoe 24th March 2019git
# Solution to 2019 problem 10

# Task
# Write a program that displays a plot of the functions x, x**2 and 2x
# in the range [0, 4].

import numpy as np
import matplotlib.pyplot as plot

x = np.array([0,1,2,3,4])   # make an array for the x-axis
plot.xlabel('x')   # label the x-axis, adapted from https://matplotlib.org/users/pyplot_tutorial.html
plot.ylabel('f(x) = x, x**2, 2**x')  # label the y-axis adapted from https://matplotlib.org/users/pyplot_tutorial.html
plot.title('Problem 10')   # Give title to plots, adapted from https://matplotlib.org/users/pyplot_tutorial.html

xsquared = x**2   # squares the x-axis range for f(x)=x**2

twotothex = 2**x  # multiplies the x-axis range by two

plot.plot(x,x,'b-',x,xsquared,'g^',x,twotothex,'r--') # plot the 3 functions with blue line, green triangle and red dashes
plot.show() # show the plot