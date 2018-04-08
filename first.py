class Employee(object):
	"""docstring for Employee"""
	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.email = '{}.{}@gamil.com'.format(first_name, last_name)
		self.pay = pay



	def __str__(self):
		return self.first_name
		
		



#inheritance added by ursh


#Manager and developer class
class Developer(Employee):
	annual_raise = 9

	def __init__(self,first_name,last_name,pay, lang):
		super().__init__(first_name, last_name, pay)
		self.lang = lang


class Manager(Employee):
	def __init__(self, first_name,last_name,pay, employees=None):
		super().__init__(first_name, last_name, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_employee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for em in self.employees:
			print('----->', em)
