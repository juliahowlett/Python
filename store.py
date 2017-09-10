##Store class:
##Attributes:
##• products: an array of products objects
##• location: store address
##• owner: store owner's name
##Methods:
##• add_product: add a product to the store's product list
##• remove_product: should remove a product according to the product name
##• inventory: print relevant information about each product in the store

class Store(object):
	def __init__(self, products, location, store_owner):
		self.product_list = []
		self.product_list = products
		self.location = location
		self.store_owner = store_owner
		self.inventory()
	def add_product(self, add_item):
		self.add_item = add_item
		self.product_list.append(self.add_item)
	def remove_product(self, rem_item):
		self.rem_item = rem_item
		self.product_list.remove(self.rem_item)
	def inventory(self):
		print ("\n" + ("#" * 20))
		for i in self.product_list:
			print ("Item: " + str(i))	
		#print (self.product_list)
		print ("#" * 20)
		print ("Location: " + str(self.location))
		print ("Store Owner: " + str(self.store_owner))

		
prods = ["XBox","wii","PlayStation"]		
Store1 = Store(prods, "Best Buy", "Best Guy")
Store1.add_product("IMac")
Store1.remove_product("XBox")
Store1.inventory()

