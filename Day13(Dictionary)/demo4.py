dict1 = {'dose':'set','idly':'rava','tea':'masala','coffee':'black','rice':'sambhar'}

# update(dict) - updates the current dictionary or if key is not present, it adds a new key value pair with another one
dict1.update({'lemon':'rice'})
print(dict1)
# {'dose': 'set', 'idly': 'rava', 'tea': 'masala', 'coffee': 'black', 'rice': 'sambhar', 'lemon': 'rice'}

#
dict1.update({'dose':'masala'})
print(dict1)
# {'dose': 'masala', 'idly': 'rava', 'tea': 'masala', 'coffee': 'black', 'rice': 'sambhar', 'lemon': 'rice'}


dict1['dose'] = 'onion'
print(dict1)
# {'dose': 'onion', 'idly': 'rava', 'tea': 'masala', 'coffee': 'black', 'rice': 'sambhar', 'lemon': 'rice'}

