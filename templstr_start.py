# demonstrate template string using functions
from string import Template


def main():
	# Usual string formatting with format{}
	str1 = "You're watching {0} by {1}.".format('Advanced Python', 'Paavan Gopala')
	print(str1)
	
	# TODO: create a template with placeholders
	templ = Template("You're watching ${title} by ${author}.")
	
	# TODO: use the substitute method with keywords arguments
	str2 = templ.substitute(title='Advanced Python', author='Paavan Gopala')
	print(str2)
	
	# TODO: use the substitute method with a dictionary
	data = {
		"author": "Paavan Gopala",
		"title": "Advanced Python"
	}
	str3 = templ.substitute(data)
	print(str3)
	
	
if __name__ == '__main__':
	main()