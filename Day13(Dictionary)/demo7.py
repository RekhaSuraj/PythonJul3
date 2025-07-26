d1 = {1:'red',2:'blue',3:'green'}

# d1[4] = d1[3]
# print(d1)
# d1.pop(3)
# print(d1)
# {1: 'red', 2: 'blue', 4: 'green'}

val = d1.pop(3)
print(val)
d1[4] = val
print(d1)
# {1: 'red', 2: 'blue', 4: 'green'}