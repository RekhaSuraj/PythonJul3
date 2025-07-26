# set - set is an unordered collection of unique elements,
# it does not support index
# written inside flower braces,
# insertion order is not preserved, does not allow duplicates
# Mutable - Elements must be immutable, means you cannot have a list inside a set

# Create a set
s1 = {10,20,30,40,50}
print(type(s1))
# <class 'set'>

print(s1)
# {50, 20, 40, 10, 30}

# using constructor
s2 = set({40,50,'hi','hello'})
print(type(s2))
# <class 'set'>

# create an empty set
s3 = {} # only curly brackets, interpreter considers it as dictionary object
print(type(s3))
# <class 'dict'>

s4 = set()
print(type(s4))
# <class 'set'>
print(s4)
# set()