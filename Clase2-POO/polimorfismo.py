class Perro:

	def avanzar(self):
		print("Estoy caminando")

class Ave:

	def avanzar(self):
		print("Estoy volando")


def moverse(animal):
	animal.avanzar()

perro1 = Perro()
ave1 = Ave()

moverse(perro1)
moverse(ave1)