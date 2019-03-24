# Created by Adrian Donohoe 24th March 2019
# Solution to 2019 problem 10

# Task
# Write a program that displays a plot of the functions x, x**2 and 2x
# in the range [0, 4].

import numpy as np
import matplotlib.pyplot as plot

x = np.array([0,1,2,3,4])
plot.xlabel('x')
plot.ylabel('f(x) = x, x**2, 2x')
plot.title('Problem 10')

xsquared = x**2

twox = x*2

plot.plot(x,x,'b-',x,xsquared,'g^',x,twox,'r--')
plot.show()