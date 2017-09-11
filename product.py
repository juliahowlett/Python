#  default "for sale"
class Product(object):
	def __init__(self, price, item_name, weight, brand, cost, status):
        # set some instance variables.
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand	
		self.cost = cost
		self.status = status 
		status = "for sale"
		#self.displayinfo()
	def displayinfo(self):
		print ("\n" + ("#" * 20))
		print ("Price: $" + str(self.price))
		print ("Name:" +  self.item_name)
		print ("Weight:" +  str(self.weight))
		print ("Brand:" + self.brand)	
		print ("Cost: $" + str(self.cost))
		print ("Status:" + self.status)
	def sell(self): # changes status to sold
		self.status = "sold"
		return self
	def addTax(self, tax): # takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
		self.price = self.price + (self.price * tax)
		return self
	def returnItem(self, return_reason): # takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.
		if return_reason == 'defective':
			self.status = 'defective'
			self.price = 0
		elif return_reason == 'like new':
			self.status = 'for sale'
		elif return_reason == 'opened':
			self.status = 'used'
			self.price = self.price - (self.price *0.20)
		return self			
		

if __name__ == "__main__":
	product1 = Product(450.00,"XBox",35,"MS",35,'new')
	product1.sell()
	product1.addTax(0.08)
	product1.displayinfo()
	product1.returnItem('opened').displayinfo()

if __name__ == "__main__":
	product2 = Product(250.00,"wii",15,"EA",50,"like new")
	product2.addTax(0.075).returnItem('defective').sell().displayinfo()

if __name__ == "__main__":
	product3 = Product(350.00,"PlayStation",22,"Sony",20, "defective")
	product3.addTax(0.05).displayinfo()
