

class Store(object):
	def __init__(self, location, store_owner):
		self.product_list = []
		#self.product_list = products
		self.location = location
		self.store_owner = store_owner
		#self.inventory()
	def add_product(self, *args):
		for i in args:
			if type(i) == list or type(i) == tuple:
				for k in i:
					self.product_list.append(k)
			else:
				self.product_list.append(i)
		self.inventory()		
	def remove_product(self, *args):
		for i in args:
			if type(i) == list or type(i) == tuple:
				for k in i:
					self.product_list.remove(k)
			else:
				self.product_list.remove(i)
		self.inventory()		
	def inventory(self):
		print ("\n" + ("#" * 20))
		for i in self.product_list:
			#for k in i:
			print ("Item: " + str(i))	
		#print (self.product_list)
		print ("#" * 20)
		print ("Location: " + str(self.location))
		print ("Store Owner: " + str(self.store_owner))		
		
if __name__ == "__main__":		
	prods = ["XBox","wii","PlayStation"]		
	Store1 = Store("Best Buy", "Best Guy")
	Store1.add_product(prods)
	Store1.add_product("IMac")
	Store1.remove_product("XBox")
	Store1.inventory()

