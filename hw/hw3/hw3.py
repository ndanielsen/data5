"""
HW2

Analyzing Automotive mpg data for DAT5 @GA-DC

Author: Nathan Danielsen
Email: nathanjdanielsen@gmail.com

"""
##########################################
#############    Homework    #############
##########################################
'''
Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.csv) 
to complete the following parts.  Please turn in your code for each part.  
Before each code chunk, give a brief description (one line) of what the code is
doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
the code output produces a plot or answers a question, give a brief
interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for 
group A is higher than the mean for group B which means X,Y,Z").
'''

import pandas as pd

class VroomData(object):

	def __init__(self, input_file):

		self.input_file = input_file

	def part1(self):
		'''
		Part 1
		Load the data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
		into a DataFrame.  Try looking at the "head" of the file in the command line
		to see how the file is delimited and how to load it.
		Note:  You do not need to turn in any command line code you may use.
		'''

		# How could you read the header and 

		self.df= pd.read_table(self.input_file, sep='|')


	def part2(self):

		'''
		Part 2
		Get familiar with the data.  Answer the following questions:
		- What is the shape of the data?  How many rows and columns are there?
		- What variables are available?
		- What are the ranges for the values in each numeric column?
		- What is the average value for each column?  Does that differ significantly
		  from the median?
		'''
		### I could refactor this to dictionary comprehensions later
		self.numdf = self.df._get_numeric_data()
		self.numrows = len(self.df)
		self.numcolumns = len(self.df.columns)
		self.ranges = [["Column " + "'" + col + "'" + ":" + "'" + "Max: " + str(self.numdf[col].max()) + ' , ' + "Min:" + str(self.numdf[col].min())] for col in self.numdf.columns	]
		self.averages = [["Column " + "'" + col + "'" + ":" + "'" + "Average: " + str(self.numdf[col].mean())] for col in self.numdf.columns ]
		self.median = [["Column " + "'" + col + "'" + ":" + "'" + "Median: " + str(self.numdf[col].median())] for col in self.numdf.columns ]
		self.difference = [["Column " + "'" + col + "'" + ":" + "'" + "Difference: " + str(self.numdf[col].median() - self.numdf[col].mean()) ] for col in self.numdf.columns ]

	def part3(self):
		'''
		Part 3
		Use the data to answer the following questions:
		- Which 5 cars get the best gas mileage?  
		- Which 5 cars with more than 4 cylinders get the best gas mileage?
		- Which 5 cars get the worst gas mileage?  
		- Which 5 cars with 4 or fewer cylinders get the worst gas mileage?
		'''
		self.fivebestmpg = self.df.sort('mpg', ascending=False)[:5].car_name
		self.fivewithmorethanfourbestmpg = self.df[self.df.cylinders>4].sort('mpg', ascending=False)[:5].car_name
		self.fiveworstmpg = self.df.sort('mpg', ascending=True)[:5].car_name
		self.fivewithlessthanfourworstmpg = self.df[self.df.cylinders<=4].sort('mpg', ascending=True)[:5].car_name


		

	def part4(self):
		'''
		Part 4
		Use groupby and aggregations to explore the relationships 
		between mpg and the other variables.  Which variables seem to have the greatest
		effect on mpg?
		Some examples of things you might want to look at are:
		- What is the mean mpg for cars for each number of cylindres (i.e. 3 cylinders,
		  4 cylinders, 5 cylinders, etc)?
		- Did mpg rise or fall over the years contained in this dataset?
		- What is the mpg for the group of lighter cars vs the group of heaver cars?
		Note: Be creative in the ways in which you divide up the data.  You are trying
		to create segments of the data using logical filters and comparing the mpg
		for each segment of the data.
		'''

		self.groupby_cylinders = self.df.groupby('cylinders').mean()

		self.df.groupby('model_year').mean()
		### The sweet spot for cylinders seems to be at 4

		self.df.groupby(['model_year', 'mpg']).mean().sort(ascending=True)

		self.dfgroupconclusion = "It seems that MPG has a inverse linear relationship with cylinders, displacement, horsepower, and weight. In general, also a linear relationship with model_year. "


	def main(self):
		self.part1()
		self.part2()
		self.part3()
		self.answers()

	def answers(self):




		pass



if __name__ == "__main__":

	print "hello"

	test = VroomData('auto_mpg.txt')

	test.main()

	print test.fivewithlessthanfourworstmpg