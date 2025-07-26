# print even and odd numbers in separate lists from the below list
list1 = [10,2,3,5,1,6,8,14,11,12]

even_list = []
odd_list = []

for var in list1:
    if var % 2 == 0:
        even_list.append(var)
    else:
        odd_list.append(var)

print('Even List:',even_list)
print('Odd List:',odd_list)

# Even List: [10, 2, 6, 8, 14, 12]
# Odd List: [3, 5, 1, 11]