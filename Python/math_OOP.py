class MathGenius():
	def add(self,a,b):
		print a+b
	#Silas isnt a genius yet
	def subtract(self,a,b):
		print a-b
	#Better
	def multiply(self,a,b):
		print a*b
	def divide(self,a,b):
		print a/b
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.dad = ''
		self.mom = ''
		self.school = ''
	#Returns the largest of two numbers:
	def bigger(self,a,b):
		if a>b:
			return a
		elif b>a:
			return b
		else:
			return 'They are equal'

class LanguageGenius():
	def __init__(self,name):
		self.name = name
		self.words = {}
	def backwards(self,a):
		print a[::-1]
	def define(self,word):
		if word not in self.words:
			definition = raw_input('Definition of %s: '%word)
			self.words.update({word:definition})
		else:
			print "'"+word+"'" + " Already defined"


Silas = MathGenius('Silas',13)
Silas.add(2,4)
Silas.subtract(9292,323)
Silas.multiply(3243,333)
Silas.divide(2333,43)

print Silas.name
print Silas.age
Silas.school='ieie'
print Silas.school
print Silas.bigger(100,101)

Molly = LanguageGenius('Moll')
Molly.backwards('Hello')
Molly.define('kamira')
Molly.define('door')
Molly.define('door')
print Molly.words

# Create a class for the LagnaugeGenius. Think of some homework subjects that your Language genius could do for you.
# Implement the necessary functions and variables in your class.
