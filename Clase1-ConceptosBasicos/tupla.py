my_tuple = 1,2,3,4,5
print(my_tuple)
my_tuple = (1,2,3,4,5)
print(my_tuple)
my_tuple = tuple([1,2,3,4,5])
print(my_tuple)
my_tuple = tuple(list(range(1,6)))
print(my_tuple)
my_tuple[0] = 100
print(my_tuple[:4:2])
print(my_tuple)
print(10 in my_tuple)

# Concatenacion de tuplas
tupla1 = (1,2,3,"Jean")
tupla2 = (7,8,9)
print(tupla1 + tupla2)