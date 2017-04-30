

class Patient(object):
	def __init__(self, id, name, allergies, bednmber="None"):
		self.id = id
		self.name = name
		self.allergies = allergies
		self.bednmber = None
	pass

class Hospital(object):
	def __init__(self, hospital_name, capacity):
		self.hospital_name = hospital_name
		self.capacity = capacity
		self.paitients = []
		self.bed_lsit= []

	def admit(self,name):
		if len(self.bed_lsit)<self.capacity:

		self.paitients.append(name)

		print self.paitients
		print len(self.paitients)


		


		
hospital1 = Hospital("kissimmee",10)
hospital1.admit(Patient(1, 'Matt', 'none'))
print hospital1.paitients[0].name

# hospital1 = Hospital("kissimmee",10)
hospital1.admit(Patient(1, 'Matt', 'none'))
for patient in hospital1.paitients:
	print patient.name
# print hospital1.paitients[0].name





