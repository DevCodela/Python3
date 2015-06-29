def my_function():
	print("Esta es mi funcion")

# my_function()

def sumar(number1, number2 = 100):
	"""
	Esta funcion recibe dos parametros y por defecto 
	el segundo es 100
	"""
	print(number1)
	print(number2)
	return number1 + number2

# print(sumar(number1 = 10, number2 = 5))
# print(sumar(number2 = 10, number1 = 5))
print(sumar(number1 = 10))
print(sumar.__doc__)