class Things():
	pass

class Inanimate(Things):
	pass
	
class Animate(Things):
	pass
	
class Sidewalks(Inanimate):
	pass
	
class Animals(Animate):
	pass
	
class Mammals(Animals):
	pass
	
class Dog(Mammals):
	"""a simple attempt to model a dog"""
	
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age
		 
		def sit(self):
			"""Simulate a dog sitting in response to a command."""
			print(self.name.title() + " rolled over!")
			
my_dog = Dog('Samson', 2)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " +str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()
