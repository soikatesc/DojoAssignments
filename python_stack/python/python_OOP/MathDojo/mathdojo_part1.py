

class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self,*args):
		var = 0 
		for arg in args:
			var = var + arg
		self.result = self.result+var
		return self



	def subtract(self,*args):
		var = 0 
		for arg in args:
			var = var - arg
		self.result = self.result+var
		return self

	


md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result

