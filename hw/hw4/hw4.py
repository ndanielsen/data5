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

		self.df.groupby('cylinders').mpg.mean().plot(kind='bar')
		plt.title("Comparing Mean MPG for Different Numbers of Cylinders")
		plt.ylabel("MPG")
		plt.savefig('cylinders_by_mean_mpg.png', dpi=50)

		self.part1_code = 	\
		"""
		self.df.groupby('cylinders').mpg.mean().plot(kind='bar')
		plt.title("Comparing Mean MPG for Different Numbers of Cylinders")
		plt.ylabel("MPG")
		plt.savefig('cylinders_by_mean_mpg.png', dpi=50)
		"""

		self.part1_graphic =  'cylinders_by_mean_mpg.png' 

		self.part1_answer = "It seems clear that the most efficent number of cylinders is four and declines steeply after that."
		pass


	def part2(self):
		'''
		Part 2
		Use a scatter matrix to explore relationships between different numeric variables.
		'''

		self.dfnum = self.df._get_numeric_data()

		pd.scatter_matrix(self.dfnum, alpha=0.2, diagonal='hist')
		
		plt.savefig('scatter_matrix.png', dpi=250)

		self.part2_code = 	\
		"""
		self.dfnum = self.df._get_numeric_data()
		pd.scatter_matrix(self.dfnum, alpha=0.2, diagonal='hist')
		plt.savefig('scatter_matrix.png', dpi=250)

		"""
		self.part2_graphic = 'scatter_matrix.png'

		self.part2_answer = "After looking at the entire scatter plot of numeric data, it seems that MPG is the most interesting variable to compare, so I'll make another scatterplot"
		

	def part2a(self):
		'''
		Part 2
		Use a scatter matrix to explore relationships between different numeric variables.
		'''

		

		self.dfnum.groupby('mpg').mean().hist(alpha=0.5, bins=15)
		
		plt.savefig('histo_matrix_mpg.png', dpi=250)

		self.part2a_code = 	\
		"""
		self.dfnum.groupby('mpg').mean().hist(alpha=0.5, bins=15)
		plt.savefig('histo_matrix_mpg.png', dpi=250)
		"""
		self.part2a_graphic = 'histo_matrix_mpg.png'

		self.part2a_long_answer = "For acceleration, it seems clear that there is a sweet spot around 16.5 for best MPG \
		For displacement, weight and horsepower it seems clear that as they increase, MPG goes down. \
		For model year, it trends than over time the MPG gets better."
		



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

		self.part3_code = 	\
		"""
		"""

		self.part3_graphic = "http://media.giphy.com/media/13HBDT4QSTpveU/giphy.gif"

		self.part3_answer = "In progress"
	pass

	def answers(self):

		print "#GA-DC DAT5 Homework Four Visualizing Auto Data"
		print "######_With just enough illustrative code_"
		
		print "###Part 1"
		print "\n\n"
		print self.part1.__doc__
		print "\n"

		print "![%s](%s)" % ("Image", self.part1_graphic)
		print "\n"

		print self.part1_code
		print "\n"

		print "_%s_" % self.part1_answer


		print "###Part 2"
		print "\n\n"
		print self.part2.__doc__
		print "\n"

		print "![%s](%s)" % ("Image", self.part2_graphic)
		print "\n"

		print self.part2_code
		print "\n"

		print "_%s_" % self.part2_answer


		print "####Taking a closer look at MPG and how other average variables relate to it"
		print "\n"
		print "![%s](%s)" % ("Image", self.part2a_graphic)
		print "\n"

		print self.part2a_code
		print "\n"

		print "_%s_" % self.part2a_long_answer


		print "###Part 3"
		print "\n\n"
		print self.part3.__doc__
		print "\n"

		print "![%s](%s)" % ("Image", self.part3_graphic)
		print "\n"

		print self.part3_code
		print "\n"

		print "_%s_" % self.part3_answer
		pass



	def main(self):

		self.setUP()
		self.part1()
		self.part2()
		self.part2a()
		self.part3()
		self.answers()

		### How can I auto generate a report without using the CLI?

		# with open("readme.md", 'w+') as f:
		# 	f.write(self.answers())


if __name__ == "__main__":

	print "~~Hello World!~~"

	test = VizCar("auto_mpg.txt")

	test.main()