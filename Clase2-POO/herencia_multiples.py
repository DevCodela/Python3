class Mother:

	def __init__(self, name):
		self.name = name

	def set_permission(self, child):
		if child.age >= 18:
			return True
		else:
			return False

class Father:

	def __init__(self, name):
		self.name = name

	def set_permission(self, child):
		if child.gender == "male" and child.age >= 18:
			return True
		else:
			return False

class Child(Father, Mother):

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def go_party(self, mother, father):
		if self.get_permission(mother) and self.get_permission(father):
			print("Tengo permisooo!!")
		else:
			print("No tengo permisoo")

	def get_permission(self, parent):
		return parent.set_permission(self)

gladys = Mother("Gladys")
oscar = Father("Oscar")

jean = Child("Jean Carlos", 17, "male")
mary = Child("Mary", 20, "female")

jean.go_party(gladys, oscar)
mary.go_party(gladys, oscar)
