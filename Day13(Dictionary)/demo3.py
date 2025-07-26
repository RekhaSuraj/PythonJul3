dict1 = {'Emp':'Anuhya','Salary':50000,'Company':'TCS','Location':'BLR'}

# update values
dict1['Salary'] = 60000
print(dict1)
# {'Emp': 'Anuhya', 'Salary': 60000, 'Company': 'TCS'}

# pop(key) - Remove specified key and return the corresponding value.
val = dict1.pop('Location')
print(val)

print(dict1)
# {'Emp': 'Anuhya', 'Salary': 60000, 'Company': 'TCS'}

# Removes the last Key:Value pair from dict
dict1.popitem()
print(dict1)
# {'Emp': 'Anuhya', 'Salary': 60000}

d2 = dict1.copy()
print(d2)
# {'Emp': 'Anuhya', 'Salary': 60000}

# clear() - Clears all the key value pairs and returns an empty dictionary
d2.clear()
print(d2)
# {}