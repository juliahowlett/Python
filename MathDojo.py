#perform 0+2+(2+5)-(3+2) and return 4.
#md.add(2).add(2,5).subtract(3,2).result

class MathDojo(object):
	def __init__(self):
		self.result = 0
	def add(self, *args):
		for i in args:
			self.result += i
		return self
	def subtract(self, *args):
		for i in args:
			self.result -= i
		return self
	def result(self):	
		print ("Result =" + str(self.result))
		
		
md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result		
		

		
		

	