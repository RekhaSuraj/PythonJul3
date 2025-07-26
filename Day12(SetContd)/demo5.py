# Typecasting
list1 = [10,20,30,40]
# convert list to tuple
print('Before Conversion:',type(list1))
# Before Conversion: <class 'list'>

t1 = tuple(list1)
print(t1)
# (10, 20, 30, 40)
print('After Conversion:',type(t1))
# After Conversion: <class 'tuple'>

# Convert from tuple to list
l1 = list(t1)
print(l1)
# [10, 20, 30, 40]

# Convert from list to set
list1 = [11,22,33,44,22,11,55]
s1 = set(list1)
print(s1)
# {33, 11, 44, 22, 55}

# Convert from set to list
# Convert from set to frozenset
# Convert from frozenset to tuple