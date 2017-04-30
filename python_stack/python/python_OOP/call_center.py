
class Call(object):
	def __init__(self,unique_id, caller_name, caller_phone_number, time_of_call,reasons_for_call):
		self.unique_id = unique_id
		self.caller_name = caller_name
		self.caller_phone_number = caller_phone_number
		self.time_of_call = time_of_call
		self.reasons_for_call = reasons_for_call

	def display(self):
		print "The caller id: ",self.unique_id
		print "The caller name: ",self.caller_name
		print "The caller phone number",self.caller_phone_number
		print "Time of call",self.time_of_call
		print "Reason for call",self.reasons_for_call

class Callcenter(object):
	def __init__(self,calls):
		self.calls = calls
		# self.queue_size = len(self.calls)
		# print self.queue_size

	def add(self):
		self.calls.append()
		print calls

	def remove(self):
		calls.pop(0)
		pass

	def info():
		pass

# calls = []
# for i in range(0,8):
# 	calls.append(Call(1,2,3,4,5))
call1=Call(1,2,3,4,5)
x1=Callcenter(call1)
x1.add()



# call2=Call(1,2,3,4,5)
# call3=Call(1,2,3,4,5)

# Callcenter().add(calls)
# # x1.add(calls)
# print calls

# Callcenter(calls)

# for call in calls:
# 	# CallCenter.add(call)
# 	print call



