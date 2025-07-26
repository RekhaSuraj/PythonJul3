# Dictionary : Dictionary is used to store data in the form of key: value pairs
# Dictionaries are mutable
# Enclosed within flower braces having comma separated key: value pairs, colon is used to separate key and value in a pair
# Keys must be unique
# Duplicates are allowed for values
# It can be any datatype(heterogeneous)

# create a dictionary
# empty dictionary
dict1 = {}
print(type(dict1))
# <class 'dict'>

d1 = {1: 'red', 2:'blue', 3:'green',4:'black'}
print(type(d1))
# <class 'dict'>

print(d1)
# {1: 'red', 2: 'blue', 3: 'green', 4: 'black'}

# fetch only keys from a dictionary
print(d1.keys())
# dict_keys([1, 2, 3, 4])

#fetch only values
print(d1.values())
# dict_values(['red', 'blue', 'green', 'black'])

# fetch all items, both key and values together from a dictionary
print(d1.items())
# dict_items([(1, 'red'), (2, 'blue'), (3, 'green'), (4, 'black')])


