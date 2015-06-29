lista1 = [2,3,True,"Jean"]
lista1.append(100)
lista1.remove(2)
print(lista1)
print()
lista2 = [1,2,3]
lista3 = [6,7,8]
lista2.append(lista3)
lista2.extend(lista3)
print(lista2)
print(lista2[3][1])