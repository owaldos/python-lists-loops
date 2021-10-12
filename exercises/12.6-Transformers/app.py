incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:

def my_var(data):
	list_values=list(data.values())
	new_str= list_values[0]+' '+list_values[1]
	return new_str

	
	
transformedData= list(map(my_var,incomingAJAXData))

print(transformedData)