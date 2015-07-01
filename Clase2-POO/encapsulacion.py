class Animal:

	def __init__(self, name, age):
		self.name = name
		self.__age = age

	def get_age(self):
		return self.__age

	def set_age(self, age):
		self.__age = age

avril = Animal("Avril", 4)

print(avril.name)
print(avril.get_age())
avril.set_age(10)
print(avril.get_age())