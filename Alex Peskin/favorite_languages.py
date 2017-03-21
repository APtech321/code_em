favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'plil': 'python',
	'aidan': 'java',
	'hadley': 'java',
	'alex': 'python',
	}
print("Sarah's favorite language is" +
	favorite_languages['sarah'].title() +
	".")

for name, language in favorite_languages.title():
	print(name.title() + " 's favorite language is " +
	language.title() + ".")
