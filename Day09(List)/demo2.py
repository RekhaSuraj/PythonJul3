list1 = [10,20,30,40,'hi','hello',10.5,'welcome',6+7j]
print(len(list1))
# 9

# Index positions
print('Element at index 0:',list1[0])
print('Element at index 1:',list1[1])
print('Element at index 2:',list1[2])
print('Element at index 3:',list1[3])
print('Element at index 4:',list1[4])
print('Element at index 5:',list1[5])
print('Element at index 6:',list1[6])
print('Element at index 7:',list1[7])
print('Element at index 8:',list1[8])

# Element at index 0: 10
# Element at index 1: 20
# Element at index 2: 30
# Element at index 3: 40
# Element at index 4: hi
# Element at index 5: hello
# Element at index 6: 10.5
# Element at index 7: welcome
# Element at index 8: (6+7j)

# If we try to access elements which is not present in the list, we get the below error
# print('Element at index 9:',list1[9])
# IndexError: list index out of range
