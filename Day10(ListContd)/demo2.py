# Nested list - List inside another list
import copy

list1 = [10,20,30,['hi','hello',40],[50,60],70,80]

print(len(list1))
# 7

print(list1[0]) #10
print(list1[1]) #20
print(list1[2]) #30
print(list1[3]) #['hi', 'hello', 40]
print(list1[4]) #[50, 60]
print(list1[5]) #70
print(list1[6]) #80

print()

print(list1[3][1])
# hello

print(list1[4][0])
# 50
print('-------------')
print()
list2 = list1.copy()
print(id(list2))
print(id(list1))

print('--------------')
print(id(list1[3]))
print(id(list2[3]))
print('--------------')

list1[3][0] = 999
print(list2)
print(list1)

print()
original = [10,20,30,['hi','hello',40],[50,60],70,80]
deep = copy.deepcopy(original)

print(original)
print(deep)

original[3][0] = 99
print(original)
print(deep)

print(id(original))
print(id(deep))