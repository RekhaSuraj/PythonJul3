# discard() - Remove an element from a set if it is a member.
# Unlike set. remove(), the discard() method does not raise an exception when an element is missing from the set.

set1 = {10,20,30,40}
set1.discard(30)
print(set1)
# {40, 10, 20}

# If we try to discard() an item not present, does not raise an exception
set1.discard(99)
print(set1)
# {40, 10, 20}

# If we try to remove() an item not present, exception is raised
# set1.remove(99)
# print(set1)
# KeyError: 99