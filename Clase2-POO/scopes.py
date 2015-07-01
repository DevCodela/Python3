def example():

	message = "Este es un mensaje"

	def local_message():
		message = "Este es un mensaje Local"

	def non_local_message():
		nonlocal message
		message = "Este es un mensaje No Local"

	def global_message():
		global message
		message = "Este es un mensaje global"

	print(message)
	local_message()
	print(message)
	non_local_message()
	print(message)
	global_message()
	print(message)

example()
print(message)