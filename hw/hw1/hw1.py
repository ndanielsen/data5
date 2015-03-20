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

	def part4(self, args):
		'''
		PART 4: create a list (or set) of all unique sodas and soft drinks that they sell
		Note: just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'
		'''
		unique_elems = set()
		for item in args:
		
			elems = [order[3].strip('[]') for order in self.orders if order[2] == item]
			unique_elems.update(elems)

		return unique_elems

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

	def calories(self):
		"""
		Are vegetarians and chicken eaters less likely to get sour cream and fatty toppings than beef and other meat eaters?
		
		Do I feel like this now?
		"""
		order = self.orders[4]
		
		order =  order[3]
		order = order.split(',')
		print [item.strip('[] ') for item in order]
		# order = string.strip(order, '[]')
		



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



if __name__ == "__main__":
 
	burrito = BurritoFoo('orders.tsv')
	print burrito.part4(["Canned Soda", "Canned Soft Drink"])