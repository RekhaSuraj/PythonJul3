# from keys
keys1 = ['name','age','city']

# fromkeys(keys,value) - Create a new dictionary with keys from iterable and values set to value. If no value is given,
# it will default to None
new_dict = dict.fromkeys(keys1)
print(new_dict)
# {'name': None, 'age': None, 'city': None}

d2 = dict.fromkeys(keys1,'unknown')
print(d2)
# {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

k2 = (10,20,30)
d3 = dict.fromkeys(k2,'numbers')
print(d3)
# {10: 'numbers', 20: 'numbers', 30: 'numbers'}