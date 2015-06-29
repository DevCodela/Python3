import random

name_horse1 = input("Nombre del primer caballo: ")
name_horse2 = input("Nombre del segundo caballo: ")

horse1 = {"name" : name_horse1, "steps" : [], "win" : False}
horse2 = {"name" : name_horse2, "steps" : [], "win" : False}

def set_steps(horse, steps):
	"""
	Poner (*) dentro del atributo steps de cada caballo
	"""
	for step in range(steps):
		horse["steps"].append("*")
	print("Caballo %s avanza %d" % (horse["name"], steps))

def print_steps(horse):
	"""
	Imprimir el nombre del caballo y la cantidad de pasos
	"""
	print("%s : " % horse["name"], end = "")
	for step in horse['steps']:
		print("*", end="")
	print()

def is_winner(horse):
	"""
	Verifica si la cantidad de pasos del caballo llega a 20
	"""
	if len(horse["steps"]) >= 20:
		horse["win"] = True

turno = 1
while(len(horse1["steps"]) < 20 and len(horse2["steps"]) < 20):
	print("Turno %d" % turno)

	# Primer Caballo
	set_steps(horse1, random.randrange(5))
	is_winner(horse1)

	# Segundo Caballo
	set_steps(horse2, random.randrange(5))
	is_winner(horse2)

	# Imprimir los pasos
	print_steps(horse1)
	print_steps(horse2)
	turno += 1

print("====== Ganador ======")
if horse1['win'] and horse2['win']:
	print("%s y %s Empataron!!!" % (horse1["name"], horse2["name"]))
elif horse1['win']:
	print(horse1["name"])
else:
	print(horse2["name"])