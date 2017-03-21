responses = {}
polling_active = True
while polling_active:
	name = raw_input("What is your name? ")
	response = raw_input("Which VA stream did you take measurments? ")
	responses[name] = response
	repeat = raw_input("Is there another person on your team to respond? (yes/no ")
	if repeat == 'no':
		polling_active = False
	print ("--- Stream Visitation Results ---")
	for name, response in responses.items():
		print(name  + " took measurments at the " + response + " site.")
