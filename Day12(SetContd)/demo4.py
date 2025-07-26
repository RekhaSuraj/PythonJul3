# frozenset
# A frozenset in Python is an immutable version of a set. Once created, its elements cannot be changed.
fs = frozenset([1,2,3,4,5])
print(type(fs))
# <class 'frozenset'>

print(fs)
# frozenset({1, 2, 3, 4, 5})

# copy() - Return a shallow copy of a set
fz1 = fs.copy()
print(fz1)
# frozenset({1, 2, 3, 4, 5})

fs2 = frozenset([10,20,'hi',30.5])
print(type(fs2))
# <class 'frozenset'>
fs3 = frozenset({10,20,'hi',30.5})
print(type(fs3))
# <class 'frozenset'>

# hw -
# fs2.union()
# fs2.isdisjoint()
# fs2.issuperset()
# fs2.issubset()
# fs2.intersection()
# fs2.symmetric_difference()


