class Father:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def drive(self, child = None):
		if child is None:
			print("Estoy conduciendoo mi carro!!")
		elif child.age >= 18 and child.gender == "male":
			print("%s, puedes conducir mi carro" 
					% child.name)
		else:
			print("%s, No puedes conducir mi carro" 
				% child.name)

class Child(Father):

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def drive(self):
		print("Voy pedir permiso a mi padre")
		super(Child, self).drive(self)

oscar = Father("Oscar", 55)
# oscar.drive()
jean = Child("Jean", 17, "male")
mary = Child("Mary", 20, "female")
jean.drive()
mary.drive()