"""
HW1

Analyzing Chipotle Order Data for DAT5 @GA-DC

Author: Nathan Danielsen
Email: nathanjdanielsen@gmail.com

"""
import csv


class BurittoFoo(object):
	"""
	Made to order class to analyze mexico food, costs and ingredients.

	Data Header
	['order_id', 'quantity', 'item_name', 'choice_description', 'item_price']
	"""


	def __init__(self, file):
		self._file = open(file, 'rU') # is there a better way to do this?

		self.data = [line for line in csv.reader(self._file, delimiter='\t')]

		self.header = self.data[0]

		self.orders = self.data[1:]

		self.totalcost = sum([float(row[4][1:].strip(' ')) for row in self.orders])

	def part1(self):
		
		'''
		PART 1: read in the data, parse it, and store it in a list of lists called 'data'
		Hint: this is a tsv file, and csv.reader() needs to be told how to handle it
		'''
		return self.datadump

	def part2(self):
		'''
		PART 2: separate the header and data into two different lists
		'''
		return self.header, self.data

	def part3(self):

		'''
		PART 3: calculate the average price of an order
		Hint: examine the data to see if the 'quantity' column is relevant to this calculation
		Hint: work smarter, not harder! (this can be done in a few lines of code)
		'''
		return self.totalcost / len(self.orders)

	def part4(self):
		'''
		PART 4: create a list (or set) of all unique sodas and soft drinks that they sell
		Note: just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'
		'''
		pass


	def part5(self):
		'''
		PART 5: calculate the average number of toppings per burrito
		Note: let's ignore the 'quantity' column to simplify this task
		Hint: think carefully about the easiest way to count the number of toppings
		Hint: 'hello there'.count('e')
		'''
		pass

	def part6(self):
		'''
		PART 6: create a dictionary in which the keys represent chip orders and
		  the values represent the total number of orders
		Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
		Note: please take the 'quantity' column into account!
		Advanced: learn how to use 'defaultdict' to simplify your code
		'''
		pass 



	def answers(self):
		pass




if __name__ == "__main__":
	print "hello"
	assert 1+1 == 2

	burrito = BurittoFoo('orders.tsv')
	print burrito.part3()