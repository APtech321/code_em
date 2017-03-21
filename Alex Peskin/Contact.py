contact = ('first_name','last_name','mobile_phone','home_phone','zip_code')
def create_contact(first_name,last_name,mobile_phone,home_phone=None,zip_code=None):
	return (first_name,last_name,mobile_phone,home_phone,zip_code)
contacts = []
contacts.append(create_contact("Sue","Simmons","804-555-1234"))
contacts.append(create_contact("John","Doe","804-555-1234","804-555-1235"))
contacts.append(create_contact("Pat","Petri","804-555-1237","804-555-1238","23117"))
def find_contact_by_first_name(first_name):
	for contact in contacts:
		if contact[0] == first_name:
			return contact
	
contact = find_contact_by_first_name("John")
	
	
FIRST_NAME = 0
LAST_NAME = 1
MOBLIE_PHONE = 2
HOME_PHONE = 3
ZIP_CODE = 4
	
def find_contact_by_first_name(first_name):
	for contact in contacts:
		if contact[FIRST_NAME] == first_name:
			return contact
		
contact = find_contact_by_first_name("John")
		
def find_contact_by_last_name(last_name):
	for contact in contacts:
		if contact[LAST_NAME] == last_name:
			return contact
contact = find_contact_by_last_name("Simmons")

contacts_by_last_name = {}

for contact in contacts:
	contacts_by_last_name[contact[LAST_NAME]] = contact
	
contact = contacts_by_last_name["Simmons"]

contacts_by_first_name = {}

for contacts in contacts:
	contacts_by_first_name[contact[FIRST_NAME]] = contact

print contacts_by_first_name
print contact

contact = contacts_by_first_name["Sue"]

def add_contact(contact):
	contacts_by_first_name[contact[FIRST_NAME]] = contact
	contacts_by_last_name[contact[LAST_NAME]] = contact
	
add_contact(create_contact("Bart","Simpson","804-555-4321"))

contact = contacts_by_first_name["Bart"]

contact = contacts_by_last_name["Simpson"]


print ("Would you like a new contact")
answer = str(raw_input())
if answer == "yes":
	print ("What is the first name")
	firstname = str(raw_input())
	print ("What is last name")
	lastname = str(raw_input())
	print ("What is the zip code")
	zipcode = str(raw_input())
	print ("What is the house number")
	housenumber = str(raw_input())
	print ("What is cell phone")
	cellphone = str(raw_input())
	print ("Contact Saved!")
	contacts.append(create_contact(firstname, lastname, cellphone, housenumber, zipcode))
	print contactss
