pizza = {
	'crust': 'thick',
	'toppings': ['extra cheese','bacon','olives','meatballs'],
	}
print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the following toppings: ")
for topping in pizza['toppings']:
	print("\t" + topping)

