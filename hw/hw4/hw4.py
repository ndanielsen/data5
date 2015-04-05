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

		self.setUP_code = "self.df = pd.read_table(self.input_file, sep='|')" 

	def part1(self):
		'''
		Part 1
		Produce a plot that compares the mean mpg for the different numbers of cylinders.
		'''

		self.df.groupby('cylinders').mpg.mean().plot(kind='bar')
		plt.title("Comparing Mean MPG for Different Numbers of Cylinders")
		plt.ylabel("MPG")
		plt.savefig('cylinders_by_mean_mpg.png', dpi=50)
		plt.close()

		self.part1_code = 	\
		"""
		self.df.groupby('cylinders').mpg.mean().plot(kind='bar')
		plt.title("Comparing Mean MPG for Different Numbers of Cylinders")
		plt.ylabel("MPG")
		plt.savefig('cylinders_by_mean_mpg.png', dpi=50)
		plt.close()
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

		plt.close()

		self.part2_code = 	\
		"""
		self.dfnum = self.df._get_numeric_data()
		pd.scatter_matrix(self.dfnum, alpha=0.2, diagonal='hist')
		plt.savefig('scatter_matrix.png', dpi=250)
		plt.close()
		"""
		self.part2_graphic = 'scatter_matrix.png'

		self.part2_answer = "After looking at the entire scatter plot of numeric data, it seems that MPG is the most interesting variable to compare, so I'll make another scatterplot"
		

	def part3(self):
		'''
		Part 3
		Use a plot to answer the following questions:
		-Do heavier or lighter cars get better mpg? (A)
		-How are horsepower and displacement related? (B)
		-What does the distribution of acceleration look like? (C)
		-How is mpg spread for cars with different numbers of cylinders? (D)
		-Do cars made before or after 1975 get better average mpg? (Hint: You need to 
		create a new column that encodes whether a year is before or after 1975.)
		'''

		pass
	

	def part3a(self):
		'''
		-Do heavier or lighter cars get better mpg? (A)
		-How is mpg spread for cars with different numbers of cylinders? (D)
		'''		

		self.dfnum.groupby('mpg').mean().hist(alpha=0.5, bins=15)
		
		plt.savefig('histo_matrix_mpg.png', dpi=250)

		plt.close()

		self.part3a_code = 	\
		"""
		self.dfnum.groupby('mpg').mean().hist(alpha=0.5, bins=15)
		plt.savefig('histo_matrix_mpg.png', dpi=250)
		plt.close()
		"""
		self.part3a_graphic = 'histo_matrix_mpg.png'

		self.part3a_long_answer = "For acceleration, it seems clear that there is a sweet spot around 16.5 for best MPG \
		For displacement, weight and horsepower it seems clear that as they increase, MPG goes down. \
		For model year, it trends than over time the MPG gets better."
		


	def part3b(self):
		'''
		-How are horsepower and displacement related? (B)
		'''		

		plt.scatter(self.dfnum.horsepower, self.dfnum.displacement, alpha=.5)
		plt.title("Horsepower versus Displacement")
		plt.xlabel("Horsepower")
		plt.ylabel("Displacement")
		plt.savefig('scatter_horsepower_vs_displacement.png', dpi=250)
		plt.close()

		self.part3b_code = 	\
		"""
		plt.scatter(self.dfnum.horsepower, self.dfnum.displacement, alpha=.5)
		plt.title("Horsepower versus Displacement")
		plt.xlabel("Horsepower")
		plt.ylabel("Displacement")
		plt.savefig('scatter_horsepower_vs_displacement.png', dpi=250)
		plt.close()

		"""
		self.part3b_graphic = 'scatter_horsepower_vs_displacement.png'

		self.part3b_long_answer = "In general, as horsepower increases the displacement increases."


	def part3c(self):
		'''
		-What does the distribution of acceleration look like? (C)
		'''		

		self.dfnum.acceleration.hist(bins=30)
		plt.title("Distribution of Acceleration")
		plt.savefig('hist_acceleration.png', dpi=250)
		plt.close()

		self.part3c_code = 	\
		"""
		self.dfnum.acceleration.hist(bins=30)
		plt.title("Distribution of Acceleration")
		plt.savefig('hist_acceleration.png', dpi=250)
		plt.close()

		"""
		self.part3c_graphic = 'hist_acceleration.png'

		self.part3c_long_answer = "Acceleration looks normally distributed"

		pass

	def part3d(self):
		'''
		-Do cars made before or after 1975 get better average mpg? (Hint: You need to 
		create a new column that encodes whether a year is before or after 1975.)
		'''		

		def f (x):
			if x < 75:
				return True 
			else:
				return False	

		self.dfnum["before_75"] = self.dfnum.model_year.apply(f)

		self.dfnum.groupby('before_75').mpg.mean().plot(kind='barh')
		plt.xlabel("MPG")
		plt.ylabel("")
		plt.yticks((1, 0),('Before 1975', '1975 and After'))
		plt.title("Average MPG of Cars before and after 1975")
		plt.savefig('seventy_five_divide_mgp.png', dpi=150)
		plt.close()

		self.part3d_code = 	\
		"""
		def f (x):
			if x < 75:
				return True 
			else:
				return False	

		self.dfnum["before_75"] = df.model_year.apply(f)

		df.groupby('before_75').mpg.mean().plot(kind='barh')
		plt.xlabel("MPG")
		plt.ylabel("")
		plt.yticks((1, 0),('Before 1975', '1975 and After'))
		plt.title("Average MPG of Cars before and after 1975")
		plt.close()

		"""
		self.part3d_graphic = 'seventy_five_divide_mgp.png'

		self.part3d_long_answer = "After 1975 the average MPG increases."

		pass

	def partbonus(self):
		'''
		Look at MPG by Automobile Maker and see if anything else interesting pops out
		'''

		def f (x):
			y = x.split()
			return y[0]

		self.df['make'] = self.df.car_name.apply(f)
		
		self.df.groupby(['make']).mpg.mean()

		self.partbonus1 = "So looking at the data, it seems there there are some errors in spelling of car make names the data for each type of vehicle, for example: chevroelt, toyouta, vokswagen   "

		def clean(x):
			clean_up = [("chevroelt", "chevrolet"), ("vokswagen","volkswagen"), ("vw","volkswagen"), ("mercedes-benz", "mercedes"), ("maxda", "mazda"), ("toyouta", "toyota")]    	
			y = x.split()
			for make in clean_up:

				if y[0] == make[0]:
					y[0] = y[0].replace(y[0], make[1])

			return " ".join(y)

		self.df['clean_car_name'] = self.df.car_name.apply(clean)

		self.df['make'] = self.df.clean_car_name.apply(f)


		self.partbonus2 = self.df.groupby(['make', 'model_year']).mpg.mean()

		self.partbonus_graphic = 'https://camo.githubusercontent.com/400202d86d7c3bed0e590cabe821ec7f2ce96dee/687474703a2f2f6d656469612e67697068792e636f6d2f6d656469612f31334842445434515354707665552f67697068792e676966'

		self.partbonus_code = 	""" """

	
	def answers(self):

		print "#GA-DC DAT5 Homework Four Visualizing Auto Data"
		print "######_With just enough illustrative code_"

	
		# print "###Set Up"
		# print "\n\n"
		# print self.setUP.__doc__
		# print "\n"

		# print "_%s_" % self.setUP_code
		# print "\n"




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


		print "###Part 3"
		print "\n\n"
		print self.part3.__doc__
		print "\n"

		print "####A and D \n"

		print self.part3a.__doc__
		print "\n"
		print "![%s](%s)" % ("Image", self.part3a_graphic)
		print "\n"

		print self.part3a_code
		print "\n"

		print "_%s_" % self.part3a_long_answer

		print "####B \n"
		print self.part3b.__doc__
		print "\n"
		print "![%s](%s)" % ("Image", self.part3b_graphic)
		print "\n"

		print self.part3b_code
		print "\n"

		print "_%s_" % self.part3b_long_answer


		print "####C \n"
		print self.part3c.__doc__
		print "\n"
		print "![%s](%s)" % ("Image", self.part3c_graphic)
		print "\n"

		print self.part3c_code
		print "\n"

		print "_%s_" % self.part3c_long_answer

		print "####D \n"
		print self.part3d.__doc__
		print "\n"
		print "![%s](%s)" % ("Image", self.part3d_graphic)
		print "\n"

		print self.part3d_code
		print "\n"

		print "_%s_" % self.part3d_long_answer


		print "####BONUS BABY! \n"
		print self.partbonus.__doc__
		print "\n"
		print "![%s](%s)" % ("Image", self.partbonus_graphic)
		print "\n"

		print self.partbonus_code
		print "\n"

		print "_%s_" % self.partbonus1

		print self.partbonus2


	def main(self):

		self.setUP()
		self.part1()
		self.part2()
		self.part3()
		self.part3a()
		self.part3b()
		self.part3c()
		self.part3d()
		self.partbonus()
		self.answers()

		### How can I auto generate a report without using the CLI?

		# with open("readme.md", 'w+') as f:
		# 	f.write(self.answers())


if __name__ == "__main__":

	print "~~Hello World!~~"

	test = VizCar("auto_mpg.txt")

	test.main()