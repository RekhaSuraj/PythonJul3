l1 = [40,10,5,25,55,30,45]
# sort() - Sort the list in ascending order and return None.

l1.sort()
print(l1)
# [5, 10, 25, 30, 40, 45, 55]

# sorted(iterable) - Return a new list containing all items from the iterable in ascending order
l2 = [50,30,65,10,35,15]
res_list = sorted(l2)
print(res_list)

print(l2)

# reverse order using sorted
rev_sort = sorted(l2,reverse=True)
print('reverse-sort',rev_sort)
# reverse-sort [65, 50, 35, 30, 15, 10]


# sorting in reverse order/decreasing order
l1.sort(reverse=True)
print(l1)
# [55, 45, 40, 30, 25, 10, 5]

l1.sort(reverse=True)
print('Reverse again',l1)
# Reverse again [55, 45, 40, 30, 25, 10, 5]

# Key Differences:
# Feature	                    sort()	            sorted()
#
# Modifies original list?	    ✅ Yes	            ❌ No
# Returns new list?	            ❌ No	            ✅ Yes
# Works with lists only?	    ✅ Yes	            ❌ No (works with any iterable)
# Memory efficient?	            ✅ Yes	            ❌ No (creates new object)

# clear() - removes all items in the list, but does not delete the list(empty list)
l1.clear()
print(l1)
# []