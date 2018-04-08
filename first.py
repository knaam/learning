class Employee(object):
	"""docstring for Employee"""
	#user 1 will add class variables

	company_name = 'XYZ Software Oy'
	annual_raise = 0.3

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.email = '{}.{}@gamil.com'.format(first_name, last_name)
		self.pay = pay


	def apply_raise(self):
		return Employee.annual_raise * self.pay

	def __str__(self):
		return self.first_name

	@classmethod
	def set_raise(cls, new_raise):
		cls.annual_raise = new_raise

	@classmethod
	def from_string(cls,employee_string):
		fname, lname, pay = employee_string.split('-')
		return cls(fname, lname, pay)

	@classmethod
	def from_comma_seperated(cls,comma_seperated):
		fname,lname,pay=comma_seperated.split(',')
		return cls(fname,lname,pay)

	@staticmethod
	def is_working_day(num):
		if num == 23:
			return True
		return False
		
