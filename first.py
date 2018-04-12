class Employee(object):
	"""docstring for Employee"""
	#user 1 will add class variables

	company_name = 'XYZ Software Oy'
	annual_raise = 0.3

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		#self.email = '{}.{}@gamil.com'.format(first_name, last_name)
		self.pay = pay


	@property
	def email(self):
		return ('{}{}.email.com'.format(self.first_name, self.last_name))

	@property
	def full_name(self):
		return ('{} {}'.format(self.first_name, self.last_name))
	@full_name.setter
	def full_name(self, new_name):
		self.first_name, self.last_name = new_name.split(' ')

	def apply_raise(self):
		return self.annual_raise * self.pay

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

	
		

#This will mark the changes from the original author

#Some changes here as well
#This is the line added by master branch --
#I also add this here 
#Simulate merge conflict here and I have also added these line here. 


