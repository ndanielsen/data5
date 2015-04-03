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
	'''
	Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
	to complete the following parts.  Please turn in your code for each part.  
	Before each code chunk, give a brief description (one line) of what the code is
	doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
	the code output produces a plot or answers a question, give a brief
	interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for 
	group A is higher than the mean for group B which means X,Y,Z").
	'''

	def __init__(self, input_file):

		self.input_file = input_file
		pass

	def setUP(self):
		'''
		Setup loads a CSV into a pandas dataframe. 
		'''

		self.df = pd.read_table(self.input_file, sep='|')

	def part1(self):

		'''
		Part 1
		Produce a plot that compares the mean mpg for the different numbers of cylinders.
		'''

		self.part1_graphic = "Graphic"

		self.part1_answer = "Something"
		pass


	def part2(self):

		'''
		Part 2
		Use a scatter matrix to explore relationships between different numeric variables.
		'''
		self.part2_graphic = "Graphic"

		self.part2_answer = "Something"
		pass


	def part3(self):
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

		self.part3_graphic = "Graphic"

		self.part3_answer = "Something"
	pass

	def answers(self):

		print "#GA-DC DAT5 Homework Four Visualizing Auto Data"
		print "######_With just enough illustrative code_"


		print "###Part 1"
		print "\n\n"
		print self.part1.__doc__
		
		print "\n"
		print self.part1_graphic 
		print "\n"

		print "_" + self.part1_answer +"_"


		print "###Part 2"
		print "\n\n"
		print self.part2.__doc__

		print "\n"
		print self.part2_graphic 
		print "\n"

		print "_" + self.part2_answer +"_"


		print "###Part 3"
		print "\n\n"
		print self.part3.__doc__

		print "\n"
		print self.part3_graphic
		print "\n"

		print "_" + self.part3_answer + "_"
		pass



	def main(self):

		self.part1()
		self.part2()
		self.part3()
		self.answers()

		### How can I auto generate a report without using the CLI?

		# with open("readme.md", 'w+') as f:
		# 	f.write(self.answers())


if __name__ == "__main__":

	print "~~Hello World!~~"

	test = VizCar("auto_mpg.txt")

	test.main()