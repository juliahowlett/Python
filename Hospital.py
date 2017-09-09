from random import randint

class Patient(object):
	def __init__(self, id, name, allergies):
		self.id = id
		self.name = name
		self.allergies = allergies
	def patientInfo(self):
		print ("ID: " + str(self.id))
		print ("Patient: " + self.name)
		print ("Allergies: "+ self.allergies)

class Hospital(object):
	def __init__(self, hospital_name, capacity):
		self.patient_list = []
		self.hospital_name = hospital_name
		self.capacity = capacity
		self.bed_number = 0
	def hospitalInfo(self):
		print ("Name: " + self.hospital_name)
		print ("Capacity: " + str(self.capacity))	
	def admit(self, patient): 
		self.patient = patient
		self.bed_number = randint(0,17)	
		spl = self.patient_list
		spl.append(self.patient)
		self.count = len(spl)
		if self.count > self.capacity:
			print (self.hospital_name + " is full!")
			self.bed_number = 0
		else:
			print ( "Welcome to", self.hospital_name, "hospital!" , self.capacity - self.count, "beds open!")
			print ("You will be in bed number " + str(self.bed_number))
			print (str(self.count))
		return self
	def discharge(self, dispatient):  # myList.remove("Yes")
		self.dispatient = dispatient
		self.patient_list.remove(self.dispatient)
		self.bed_number = 0
		return self	

patient1 = Patient(22, "MaryAnne", "Coconuts")		
patient1.patientInfo()

patient2 = Patient(2, "Gilligan", "Penicilin")	
patient2.patientInfo()	

patient3 = Patient(11, "Professor", "Ginger")	
patient3.patientInfo()	

patient4 = Patient(5, "Skipper", "nothing")	
patient4.patientInfo()	

patient5 = Patient(42, "Lovey", "")	
patient5.patientInfo()

patient6 = Patient(8, "Ginger", "solitude")	
patient6.patientInfo()

patient7 = Patient(13, "The Millioniare", "Tylenol")	
patient7.patientInfo()

hospital1 = Hospital("Tallahassee General", 6)
hospital1.hospitalInfo()

hospital1.admit(patient1)
hospital1.admit(patient2)
hospital1.admit(patient3)
hospital1.admit(patient4)
hospital1.admit(patient5)
hospital1.admit(patient6)
hospital1.admit(patient7)

hospital1.discharge(patient2)
hospital1.discharge(patient4)
hospital1.admit(patient7)