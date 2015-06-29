for i in range(5,10,2):
	print(i)

print()

my_list = [1,2,3,4,5,"Jean Carlos"]
for element in my_list:
	print(element)

print()

for i in range(100000):
	if i == 20:
		break
	elif i == 15:
		continue
	else:
		print(i)