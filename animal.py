class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):	
		print ("Health =" + str(self.health))
		
animal1 = Animal("Furry")
animal1.walk().walk().walk().run().run().displayHealth()
#animal1.pet()	
		
class Dog(Animal):
	def __init__(self,name):
		super(Dog, self).__init__(name)
		self.health = 150      
	def pet(self):
		self.health += 5
		print ("I am a Dog")
		return self	
		
dog1 = Dog("Ruffy")
dog1.displayHealth()
dog1.walk().walk().walk().run().run().pet().displayHealth()
#dog1.fly()		

class Dragon(Animal):
	def __init__(self,name):
		super(Dragon, self).__init__(name)	
		self.health = 170
		
	def fly(self):
		self.health -= 10
		return self	
	def dragonHealth(self):
		print ("I am a Dragon")
		super(Dragon, self).displayHealth() 

dragon1 = Dragon("Spike")
dragon1.dragonHealth()
dragon1.walk().run().run().fly().fly().dragonHealth()
#dragon1.pet()
	