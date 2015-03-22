#!/usr/local/bin/python

import unittest
from hw1 import BurritoFoo

class TestBurrito(unittest.TestCase):

	def setUp(self):
		self.burrito = BurritoFoo('head_orders.tsv')
		self.orders = self.burrito.orders
	
	def test_the_world_is_sane(self):
		self.assertEquals(1+1, 2)


	def test_toppings(self):

		self.assertEquals(self.burrito.toppings("Burrito"), (1, 8, 1) )
		self.assertEquals(self.burrito.toppings("Chicken"), (2, 11, 3) )
		self.assertEquals(self.burrito.toppings("chips"), (3, 0, 3))
		self.assertEquals(self.burrito.toppings('tacos'), (1, 5, 1) )

	def test_description_cleaner(self):

		self.assertEquals(self.burrito.description_cleaner(self.orders[0]), [])
		self.assertEquals(self.burrito.description_cleaner(self.orders[1]), ['clementine'])
		self.assertEquals(self.burrito.description_cleaner(self.orders[2]), ['apple'])
		self.assertEquals(self.burrito.description_cleaner(self.orders[3]), [])
		self.assertEquals(self.burrito.description_cleaner(self.orders[4]), ['tomatillo-red chili salsa (hot)', 'black beans', 'rice', 'cheese', 'sour cream'])
		self.assertEquals(self.burrito.description_cleaner(self.orders[5]), ['fresh tomato salsa (mild)', 'rice', 'cheese', 'sour cream', 'guacamole', 'lettuce'])
		self.assertEquals(self.burrito.description_cleaner(self.orders[6]), [])
		self.assertEquals(self.burrito.description_cleaner(self.orders[7]), ['tomatillo red chili salsa', 'fajita vegetables', 'black beans', 'pinto beans', 'cheese', 'sour cream', 'guacamole', 'lettuce'])
		self.assertEquals(self.burrito.description_cleaner(self.orders[8]), ['tomatillo green chili salsa', 'pinto beans', 'cheese', 'sour cream', 'lettuce'])	

	def test_item_filter(self):
		self.assertEquals(len(self.burrito.item_filter('Steak')), 2 ) 
		self.assertEquals(len(self.burrito.item_filter('Bowl')), 2 ) 
		self.assertEquals(len(self.burrito.item_filter('Izze')), 1 ) 
		self.assertEquals(len(self.burrito.item_filter('Veggie')), 0 )

	def test_extra_fat_score(self):
		self.assertEquals(self.burrito.extraFatScore(self.orders), 10)
		self.assertEquals(self.burrito.extraFatScore(self.orders[6]), 0)

	def test_part1andpart2(self):

		self.assertEquals(self.burrito.data[0], self.burrito.header)
		self.assertEquals(self.burrito.data[1:], self.burrito.orders)
		self.assertEquals(self.burrito.header, ['order_id', 'quantity', 'item_name', 'choice_description', 'item_price'])
		self.assertEquals(self.burrito.orders, [['1', '1', 'Chips and Fresh Tomato Salsa', 'NULL', '$2.39 '], ['1', '1', 'Izze', '[Clementine]', '$3.39 '], ['1', '1', 'Nantucket Nectar', '[Apple]', '$3.39 '], ['1', '1', 'Chips and Tomatillo-Green Chili Salsa', 'NULL', '$2.39 '], ['2', '2', 'Chicken Bowl', '[Tomatillo-Red Chili Salsa (Hot), [Black Beans, Rice, Cheese, Sour Cream]]', '$16.98 '], ['3', '1', 'Chicken Bowl', '[Fresh Tomato Salsa (Mild), [Rice, Cheese, Sour Cream, Guacamole, Lettuce]]', '$10.98 '], ['3', '1', 'Side of Chips', 'NULL', '$1.69 '], ['4', '1', 'Steak Burrito', '[Tomatillo Red Chili Salsa, [Fajita Vegetables, Black Beans, Pinto Beans, Cheese, Sour Cream, Guacamole, Lettuce]]', '$11.75 '], ['4', '1', 'Steak Soft Tacos', '[Tomatillo Green Chili Salsa, [Pinto Beans, Cheese, Sour Cream, Lettuce]]', '$9.25 ']])

	def test_part3(self):
		self.assertEquals(self.burrito.totalcost, 62.21)
		self.assertEquals(self.burrito.numtransactions, 4)
		self.assertEquals(self.burrito.part3(), (62.21/4))


	def test_part4(self):
		self.assertEquals(self.burrito.part4(["Canned Soda", "Canned Soft Drink"]), [] )
		self.assertEquals(self.burrito.part4(["Steak Burrito"]), ['pinto beans', 'cheese', 'tomatillo red chili salsa', 'guacamole', 'fajita vegetables', 'lettuce', 'black beans', 'sour cream']
)

	def test_part5(self):

		self.assertEquals(self.burrito.part5("Burrito"), 8)
		self.assertEquals(self.burrito.part5("Chicken"), 5.5)

	def test_part6(self):

		self.assertEquals(self.burrito.part6('Chips'), {'Chips and Fresh Tomato Salsa':1, 'Chips and Tomatillo-Green Chili Salsa':1, 'Side of Chips':1})
		self.assertEquals(self.burrito.part6('Chicken'), {'Chicken Bowl':3} )
		self.assertEquals(self.burrito.part6('Steak'), {'Steak Soft Tacos':1, "Steak Burrito":1} )

	def test_bonus(self):
		self.assertEquals(len(self.burrito.item_filter("Veggie")), 0)
		self.assertEquals(len(self.burrito.item_filter("Steak")), 2)
		self.assertEquals(len(self.burrito.item_filter("Chicken")), 2)
