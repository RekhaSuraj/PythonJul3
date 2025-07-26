# For loop in a tuple
t1 = (11,22,33,44,55,66,77)
for t in t1:
    print(t)

# 11
# 22
# 33
# 44
# 55
# 66
# 77

# For loop in a set
set1 = {10,20,30,'hi','GRK'}
for s in set1:
    print(s, end=',')

# GRK,20,hi,10,30,

print()
# For loop in a string
str1 = 'Hello World'

for s1 in str1:
    print(s1)

# H
# e
# l
# l
# o
#
# W
# o
# r
# l
# d

print()
# For loop in a dictionary
dict1 = {1:'abc',2:'xyz',3:'lmn'}

# looping through keys
for k in dict1:
    print(k)

# 1
# 2
# 3

print()
# loop through only values
for v in dict1:
    print(dict1[v])

# abc
# xyz
# lmn

print()
# Looping through keys and values
for k,v in dict1.items():
    print(f'{k}-{v}')

# 1-abc
# 2-xyz
# 3-lmn