print((lambda x : x + 5)(5))
def sumar(n):
	return lambda x : x + n

mi_funcion_anonima = sumar(10)
print(mi_funcion_anonima(100))