class Employee(object):
	"""docstring for Employee"""
	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.email = '{}.{}@gamil.com'.format(first_name, last_name)
		self.pay = pay



	def __str__(self):
		return self.first_name
		
		
emp_1 = Employee('Deepak', 'Panta', 15000)
emp_2 = Employee('Test', 'User', 16000)

print (emp_1.email)
print (emp_1.email)
