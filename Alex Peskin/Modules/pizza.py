def make_pizza(size, *toppings):
	print("Making a " + str(size) +
	"-inch pizza with the following toppings:")
	for toppings in toppings:
		print("-" + toppings)
