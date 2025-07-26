# set methods

set1 = {1,2,3,4}
set2 = {1,2,3}
# Update a set with the union of itself and others(Same as extend in list)
set1.update(set2)
print(set1)

a = {10,20,30}
b = {40,50,60}

a.update(b)
print(a)
# {50, 20, 40, 10, 60, 30}

# difference() - Return the difference of two or more sets as a new set.
# (i. e. all elements that are in this set but not the others.)
res = set1.difference(set2)
print(res)
# {4}

print('diff',a.difference(b))
# diff {10, 20, 30}


# difference_update() - Remove all elements of another set from this set
set1.difference_update(set2)
print(set1)
# {4}

# If both sets are same, we get an empty set
print({1,2,3}.difference({1,2,3}))
# set()