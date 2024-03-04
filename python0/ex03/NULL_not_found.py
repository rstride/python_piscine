def NULL_not_found(object: any) -> int:
	if type(object) == type(None) and object == None:
		print("Nothing:", object, "<class 'NoneType'>")
	elif type(object) == float and object != 0:
		print("Cheese:", object, "<class 'float'>")
	elif type(object) == int and object == 0:
		print("Zero:", object, "<class 'int'>")
	elif type(object) == str and object == '':
		print("Empty:", object, "<class 'str'>")
	elif type(object) == bool and object == False:
		print("Fake:", object, "<class 'bool'>")
	else:
		print("Type not found")
	return 1