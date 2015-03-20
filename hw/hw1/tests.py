import unittest
from hw1 import BurritoFoo

class TestBurrito(unittest.TestCase):

	def setUp(self):
		self.burrito = BurritoFoo('head_orders.tsv')
	


	def test_the_world_is_sane(self):
		self.assertEquals(1+1, 2)


	def test_part1andpart2(self):

		self.assertEquals(self.burrito.data[0], self.burrito.header)
		self.assertEquals(self.burrito.data[1:], self.burrito.orders)
		self.assertEquals(self.burrito.header, ['order_id', 'quantity', 'item_name', 'choice_description', 'item_price'])
		self.assertEquals(self.burrito.orders, [['1', '1', 'Chips and Fresh Tomato Salsa', 'NULL', '$2.39 '], ['1', '1', 'Izze', '[Clementine]', '$3.39 '], ['1', '1', 'Nantucket Nectar', '[Apple]', '$3.39 '], ['1', '1', 'Chips and Tomatillo-Green Chili Salsa', 'NULL', '$2.39 '], ['2', '2', 'Chicken Bowl', '[Tomatillo-Red Chili Salsa (Hot), [Black Beans, Rice, Cheese, Sour Cream]]', '$16.98 '], ['3', '1', 'Chicken Bowl', '[Fresh Tomato Salsa (Mild), [Rice, Cheese, Sour Cream, Guacamole, Lettuce]]', '$10.98 '], ['3', '1', 'Side of Chips', 'NULL', '$1.69 '], ['4', '1', 'Steak Burrito', '[Tomatillo Red Chili Salsa, [Fajita Vegetables, Black Beans, Pinto Beans, Cheese, Sour Cream, Guacamole, Lettuce]]', '$11.75 '], ['4', '1', 'Steak Soft Tacos', '[Tomatillo Green Chili Salsa, [Pinto Beans, Cheese, Sour Cream, Lettuce]]', '$9.25 ']])

	def test_part3(self):
		self.assertEquals(self.burrito.totalcost, 62.21)
		self.assertEquals(self.burrito.numtransactions, 4)
		self.assertEquals(self.burrito.part3(), (62.21/4))
