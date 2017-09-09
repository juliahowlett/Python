# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 
class Car(object):
	def __init__(self, price, speed, fuel, mileage):
        # set some instance variables.
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage	
		if self.price > 10000:
			self.tax = "0.15"
		else:
			self.tax = "0.12"
		self.displayinfo()
	def displayinfo(self):
		print ("Price: $" + str(self.price))
		print ("Speed:" +  str(self.speed) + ' mph')
		print ("Fuel:" +  self.fuel)
		print ("Mileage:" + str(self.mileage) + ' mpg')	
		print("Tax:" + str(self.tax))
	
				
car1 = Car(8250,35,"Full",35)

car2 = Car(22250,105,"Not Full",50)

car3= Car(35500,65,"Full", 20)

