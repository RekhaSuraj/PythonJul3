l1 = ['Anuhya','VidyaBhushan','Katyayanee','GRK']

# append() - Appends/adding object to the end of the list
l1.append('Welcome')
print(l1)
# ['Anuhya', 'VidyaBhushan', 'Katyayanee', 'GRK', 'Welcome']

# If we try to append or add more than one element, we get the below error
# l1.append('Welcome','hello')
# TypeError: list.append() takes exactly one argument (2 given)


# pop(index) - Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.
res_value = l1.pop(3)
print(res_value)

print(l1)
# ['Anuhya', 'VidyaBhushan', 'Katyayanee', 'Welcome']

# Raises IndexError if list is empty or index is out of range.
# l1.pop(4)
# IndexError: pop index out of range

# remove() - Remove first occurrence of value.
# Raises ValueError if the value is not present
res = l1.remove('Welcome')
print(res)
# None
print(l1)

# ['Anuhya', 'VidyaBhushan', 'Katyayanee']

# ValueError: list.remove(x): x not in list
# l1.remove('hi')