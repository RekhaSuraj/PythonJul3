t1 = {5,10,'hi','hello',25,30}
print(t1)

# print(t1[0])
# TypeError: 'set' object is not subscriptable

# add() - Add an element to a set.
# This has no effect if the element is already present.
t1.add(100)
print(t1)
# {'hello', 100, 5, 25, 10, 30, 'hi'}

# If we try to add an item already present, it does not give error
t1.add(10)
print(t1)
# {'hello', 100, 5, 'hi', 25, 10, 30}

# pop() - removes an item and returns the value removed
# print(t1.pop())
# print(t1)
# {5, 'hello', 25, 10, 'hi', 30}

# remove() - Remove an element from a set; it must be a member.
# t1.remove('hello')
# print(t1)
# {5, 30, 25, 10, 'hi'}

# If we try to remove an item not present in the set
# t1.remove(99)
# print(t1)
# KeyError: 99