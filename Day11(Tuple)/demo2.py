# Tuple methods - Allows only 2 methods
# count() - Return number of occurrences of a value
t1 = (11,22,33,44,22,55,22,44,'hi')

print(t1.count(22))
# 3

print(t1.count(44))
# 2

print(t1.count(66))
# 0

# index() - Return first index of value
print(t1.index(33))
# 2

print(t1.index('hi'))
# 8

