
class Call(object):
	def __init__(self, unique_id, caller_name, caller_phone, call_time, call_reason):
		self.unique_id = unique_id
		self.caller_name = caller_name
		self.caller_phone = caller_phone
		self.call_time = call_time
		self.call_reason = call_reason
		self.call = [self.unique_id, self.caller_name, self.caller_phone, self.call_time, self.call_reason]
	def display(self):
		print ("ID: " + str(self.unique_id))
		print ("Call: " + self.caller_name)
		print ("Caller phone: "+ self.caller_phone)
		print ("Call Time: " + self.call_time)
		print ("Reason: " + self.call_reason)
		print (self.call)

class CallCenter(object):
	def __init__(self):
		#self.call = []
		self.queue = []
		self.queue_size = 0
	def add(self, call):
		self.call = [call]
		#self.queue + self.call
		#self.queue.insert(0, call)
		self.queue_size + 1
		print (self.queue)
		return self
	def remove(self):  	
		self.queue(pop)
		self.queue_size - 1
		return self	
	def info(self):
		print (self.queue)
		print ("name: ")
		print ("number: ")
		print ("Queue size =" + str(self.queue_size))	
		
call1 = Call(1, "MaryAnne", "555-5555", "7:34 PM", "Out of coconuts")		
call1.display()

call2 = Call(2, "Gilligan", "555-5556", "7:37 PM", "Kidnapped by an Ape")	
call2.display()		

q1 = CallCenter()
q1.add(call1)
q1.info()