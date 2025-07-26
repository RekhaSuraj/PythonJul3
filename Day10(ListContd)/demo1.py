list1 = [35,20,10,45,60,5,25,10]
# print(help(list.reverse))
# reverse() - Reverses the given string and returns None
list1.reverse()

print(list1)
# [25, 5, 60, 45, 10, 20, 35]

# count() - Return number of occurrences of value.
print(list1.count(10))
# 2

# If value is not present, count returns 0
print(list1.count(90))
# 0


# copy() - Return a shallow copy of the list
list2 = list1.copy()
print(list2)

print(id(list1))
print(id(list2))

# 2713562501504
# 2713562822720


# extend - Extend list by appending elements from the iterable
l2 = [11,22,33,44,55]
list1.extend(l2)
print(list1)
# [10, 25, 5, 60, 45, 10, 20, 35, 11, 22, 33, 44, 55]

print(l2)
# [11, 22, 33, 44, 55]

print()
l2.extend(list1)
print(l2)
# [11, 22, 33, 44, 55, 10, 25, 5, 60, 45, 10, 20, 35, 11, 22, 33, 44, 55]