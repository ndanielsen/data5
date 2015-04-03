#!/usr/local/bin/python
"""
HW4

Visualizing Automotive mpg data for DAT5 @GA-DC

Author: Nathan Danielsen
Email: nathanjdanielsen@gmail.com

##########################################
#############    Homework    #############
##########################################
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class VizCar(object):

	def __init__(self, input_file):

		self.input_file = input_file
		pass

'''
Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
to complete the following parts.  Please turn in your code for each part.  
Before each code chunk, give a brief description (one line) of what the code is
doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
the code output produces a plot or answers a question, give a brief
interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for 
group A is higher than the mean for group B which means X,Y,Z").
'''

'''
Part 1
Produce a plot that compares the mean mpg for the different numbers of cylinders.
'''

'''
Part 2
Use a scatter matrix to explore relationships between different numeric variables.
'''

'''
Part 3
Use a plot to answer the following questions:
-Do heavier or lighter cars get better mpg?
-How are horsepower and displacement related?
-What does the distribution of acceleration look like?
-How is mpg spread for cars with different numbers of cylinders?
-Do cars made before or after 1975 get better average mpg? (Hint: You need to 
create a new column that encodes whether a year is before or after 1975.)
'''

if __name__ == "__main__":

	print "Hello"