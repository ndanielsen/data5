"""
HW1

Analyzing Chipotle Order Data for DAT5 @GA-DC

Author: Nathan Danielsen
Email: nathanjdanielsen@gmail.com

"""
import csv


class BurritoFoo(object):
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

		self.numtransactions = max([int(row[0]) for row in self.orders])

		self.totalcost =  round(sum([float(row[4][1:].strip(' ')) for row in self.orders]), 2)

	
	def toppings(self, item):
		""" 
		Takes a single word 'item' noun 

		Returns the number of times the noun has shown up in order history and also the numbers of toppings 

		"""
		item = item.lower()
		item_count, toppings_count, quantity = 0, 0, 0 

		for row in self.orders: # looks at all orders
			item_name = row[2]
			item_name = item_name.lower()
			item_name = item_name.split()  


			if item in item_name:

				item_count += 1
				quantity += int(row[1])

				if row[3] != "NULL": ### Added because chips are NULL value and was making calculation problems with +1 comma correction

					toppings_count += row[3].count(',') + 1 # counting the number of commas in choice description # and assuming salsa is a topping

			else:
				pass

		return item_count, toppings_count, quantity

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
		return self.totalcost / self.numtransactions

	def part4(self):
		'''
		PART 4: create a list (or set) of all unique sodas and soft drinks that they sell
		Note: just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'
		'''
		can = "Canned Soda"
		soft = "Canned Soft Drink"

		sodaset = set([soda[3].strip('[]') for soda in self.orders if soda[2] == can or soda[2] == soft])

		return list(sodaset)

	def part5(self, item):
		'''
		PART 5: calculate the average number of toppings per burrito
		Note: let's ignore the 'quantity' column to simplify this task
		Hint: think carefully about the easiest way to count the number of toppings
		Hint: 'hello there'.count('e')
		'''



		item_count, toppings_count, quantity = self.toppings(item)



		return float(toppings_count) / item_count

	def part6(self):
		'''
		PART 6: create a dictionary in which the keys represent chip orders and
		  the values represent the total number of orders
		Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
		Note: please take the 'quantity' column into account!
		Advanced: learn how to use 'defaultdict' to simplify your code
		'''
		pass 


	def interestingquestion(self):
		"""
		Are vegetarians and chicken eaters less likely to get sour cream and fatty toppings than beef and other meat eaters?
		"""

		pass

	def answers(self):
		pass




if __name__ == "__main__":
	print "hello"
	assert 1+1 == 2



	### Testing a first values of the file 
	burrito = BurritoFoo('head_orders.tsv')
	assert burrito.numtransactions == 4
	print burrito.part5("Tacos")