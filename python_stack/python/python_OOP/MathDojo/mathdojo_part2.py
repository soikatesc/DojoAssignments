
class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self,*args):
		sum = 0 
		for arg in args:
			if type(arg)==int:
				sum = sum + arg
			elif type(arg)==list:
				for i in range(len(arg)):
					sum = sum+arg[i]


		self.result = self.result+sum
		return self



	def subtract(self,*args):
		sum = 0 
		for arg in args:
			if type(arg)==int:
				sum = sum + arg

			elif type(arg)==list:
				for i in range(len(arg)):
					sum = sum+arg[i]

		self.result = self.result-sum
		return self

	

md = MathDojo()
print md.add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result