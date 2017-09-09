# declare a class 
class Bikes(object):
	def __init__(self, price, max_speed, miles):
        # set some instance variables.
		self.price = price
		self.max_speed = max_speed
		self.miles = miles		
	def displayinfo(self):
		print ("Price:" + self.price)
		print ("Maximum Speed:" +  str(self.max_speed) + ' mph')
		print ("Total Miles:" + str(self.miles) + ' miles')
		return self	
	def ride(self):
		self.miles += 10
		print ("Riding")
		return self	
	def reverse(self):
		print ("Reversing")	
		if self.miles >= 5:
			self.miles -= 5
		return self
				
bike1 = Bikes("250.00",15,0)
bike1.ride().ride().ride().reverse().displayinfo()

bike2 = Bikes("450.00",45,0)
bike2.ride().ride().reverse().reverse().displayinfo()

bike3 = Bikes("1250.00",65,0)
bike3.reverse().displayinfo()

