class Animal:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def caminar(self):
		print("Caminando!!")

	def comer(self):
		print("Comiendo")

class Perro(Animal):

	def __init__(self, nombre, edad, raza):
		super(Perro, self).__init__(nombre, edad)
		self.raza = raza

	def ladrar(self):
		print("Guau guau!!")

avril = Perro("Avril", 1, "labrador")
print(avril.name)
avril.caminar()
avril.comer()
avril.ladrar()