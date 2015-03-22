#!/usr/local/bin/python


"""
HW1

Analyzing Chipotle Order Data for DAT5 @GA-DC

Author: Nathan Danielsen
Email: nathanjdanielsen@gmail.com

"""
import csv
from collections import defaultdict
import string



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
	
	@staticmethod
	def description_cleaner(order):
		order =  order[3]
		
		if order == "NULL":
			return []
		else:
			order = order.split(',')
			cleaned = [item.strip('[] ').lower() for item in order]
			return cleaned

	def item_filter(self, item):

		filtered_orders = []

		item = item.lower()
		
		for row in self.orders: # looks at all orders
			item_name = row[2]
			item_name = item_name.lower()
			item_name = item_name.split()  

			if item in item_name:
				filtered_orders.append(row)

		return filtered_orders


	def toppings(self, item):
		""" 
		Takes a single word 'item' noun 

		Returns the number of times the noun has shown up in order history, numbers of toppings and quantit of orders 

		"""
		item_count, toppings_count, quantity = 0, 0, 0 
  
		filtered_orders = self.item_filter(item)
		
		item_count = len(filtered_orders)

		for row in filtered_orders:
			quantity += int(row[1])
			toppings_count += len(self.description_cleaner(row))

		
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

	def part4(self, items):
		'''
		PART 4: create a list (or set) of all unique sodas and soft drinks that they sell
		Note: just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'
		'''
		unique_elems = set()
		for order in self.orders: # going through all the order data
			for item in items:
				if item == order[2]:
					description = self.description_cleaner(order)
					unique_elems.update(description)

		unique = list(unique_elems)
		return unique

	def part5(self, item):
		'''
		PART 5: calculate the average number of toppings per burrito
		Note: let's ignore the 'quantity' column to simplify this task
		Hint: think carefully about the easiest way to count the number of toppings
		Hint: 'hello there'.count('e')
		'''
		item_count, toppings_count, quantity = self.toppings(item)

		return float(toppings_count) / item_count

	def part6(self, item ):
		'''
		PART 6: create a dictionary in which the keys represent chip orders and
		  the values represent the total number of orders
		Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
		Note: please take the 'quantity' column into account!
		Advanced: learn how to use 'defaultdict' to simplify your code
		'''
		item_dict = defaultdict(int)

		# for k in s:
		# 	item_dict[k] += 1 
		item = item.lower()

		for row in self.orders: # looks at all orders
			item_name = row[2]
			item_name = item_name.lower()
			item_name = item_name.split()  
			#print row 
			if item in item_name:
				item_dict[row[2]] += int(row[1])

		return item_dict


	def extraFatScore(self, orders):
		"""
		Counts the extra fatty toppings in a set of orders and returns a score of total toppings
		"""		
		unhealthy = ['cheese', 'guacamole', 'sour cream']

		total_score = 0

		if len(orders) == 5 and type(orders[3]) == str: ### for evaluating a single order and confirming 3rd element is string, not another order
			order = orders
			fatty_sides = [side for side in unhealthy if side in self.description_cleaner(order)]
			total_score += len(fatty_sides)	

		else :
			for order in orders:
				score = len([side for side in unhealthy if side in self.description_cleaner(order)])
				total_score += score

		return total_score

	def bonus(self, query):
		"""
		Quesiton: Are vegetarians and chicken eaters less likely to get sour cream and fatty toppings than beef and other meat eaters?
		
		Funciton takes in a single string or list of strings for proteins in an order, and returns the average number of the fatty toppings [1-3]   
		"""	

		# query = ['Steak', 'Chicken', 'Veggie', 'Barbacoa', 'Carnitas']
		
		def average_fattyscore(protein):
				
				try:
					filtered_orders = self.item_filter(protein)
					fatty_score = reduce(lambda x,y : x + y, map(self.extraFatScore, filtered_orders))
					averaged_score = float(fatty_score) / len(filtered_orders)

					return protein, round(averaged_score, 2)
			
				except TypeError:
			
					return protein, None

		if type(query) == list:

			return map(average_fattyscore, query)

		else:

			return	average_fattyscore(query)			



	def answers(self):

		print "Answers to HW 1"
		print "Parts 1 and 2 are too verbose to print here"
		print '\n'
		print "Average price per order is $%s" % self.part3()
		print '\n'
		print "These are the sodas served: %s" % self.part4(["Canned Soda", "Canned Soft Drink"])
		print '\n'
		print "Average toppings per burrito is %s" % self.part5("Burrito")
		print '\n'
		print "Chips Orders and Quantity of Order Type"
		for key, value in self.part6("Chips").items():
			print key,":", value

		print '\n'
		print "My self-defined bonus question was:"
		print "Which types of proteins(Steak, Chicken, etc) have more fatty toppings like guacamole, sour cream and cheese?"
		print "Veggie as the 'main' topping was my control."
		results = self.bonus(['Steak', 'Chicken', 'Carnitas', 'Veggie', 'Barbacoa'])
		print "The results are that:"
		for protein, average in results:
			print protein, "has", average, "fatty toppings on average"

		print "My conclusion is considering the large same size that steak and carnitas orders indulge a little more on fatty toppings. Chicken eaters are less likely to order fatty toppings and are probably watching their waistlines"

if __name__ == "__main__":
 
	burrito = BurritoFoo('orders.tsv')

	print burrito.answers()

