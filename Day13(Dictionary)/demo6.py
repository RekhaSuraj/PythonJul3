d1 = {'name':'Test','age':25}


# setdefault(key,value) - setdefault(self, key, default=None, /)
#     Insert key with a value of default if key is not in the dictionary.
#     Return the value for key if key is in the dictionary, else default.
print(help(dict.setdefault))
d1.setdefault('City','BLR')
print(d1)
# {'name': 'Test', 'age': 25, 'City': 'BLR'}

print(d1.setdefault('name'))
# Test