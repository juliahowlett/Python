class Underscore(object):
	def __init__(self):
		self.result = 0
	def map(self, *args, aFun): 
		self.result = []
		self.func = aFun
		for i in args:
			if type(i) == list or type(i) == tuple:
				for k in i:
					aFun
			else:
				aFun
		print("map "+ str(self.result))		
		return self
		
		#for x in aSeq: result.append(aFunc(x))
	def reduce(self, *args):
		for i in args:
			if type(i) == list or type(i) == tuple:
				for k in i:
					self.result += k
			else:
				self.result += k
		print("reduce "+ str(self.result))		
		return self	
	def find(self, *args):
		self.list = []
		char = 'o'
		char_list = ''
		for i in (self.list):
			if i.find(char) == True:
				char_list = char_list + " " + i
		print(char_list)
		return self
	#def filter(self):
        #if isinstance(eL, int): 
		#return self
	#def reject(self): 
        # your code
		
		
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
sum = _.reduce([1, 2, 3, 4, 5, 6])
transform = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 3)
#evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above  { return num * 3; })