def make_pizza(size, *args):
	"""
	Summarize the pizza we are about to make.
	"""
	print(f'Making {size}-inch pizza with the following toppings:')
	for arg in args:
		print(f'* {arg}')
