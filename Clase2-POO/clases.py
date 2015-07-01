class Perro:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def ladrar(self):
		print("Guauu Guauuu!!")

	def comer(self):
		print("Comiendoo!!")

avril = Perro("Avril", 3)
print(avril.name)
print(avril.age)
toby = Perro("Toby", 5)
print(toby.name)
print(toby.age)