s1 = {1,2,3,4}
s2 = {1,2,3}

# intersection() - Return the intersection of two sets as a new set.
# (i. e. all elements that are in both sets.)
print(s1.intersection(s2))
# {1, 2, 3}

#issubset() Report whether another set contains this set. Returns True or False
print(s1.issubset(s2))
# False

print(s2.issubset(s1))
# True

# issuperset() - Report whether this set contains another set.
print(s1.issuperset(s2))
# True

# union() - Return the union of sets as a new set.
# (i. e. all elements that are in either set.)
print(s1.union(s2))
# {1, 2, 3, 4}


# hw -
# s1.intersection_update()
# s1.symmetric_difference()
# s1.isdisjoint()
# s1.symmetric_difference_update()
