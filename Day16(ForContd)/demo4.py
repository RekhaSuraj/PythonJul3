# print +ve and -ve numbers in separate lists
list1 = [2,5,-10,-7,12,-25,-40,40]

pos_list = []
neg_list = []
for var in list1:
    if var > 0:
        pos_list.append(var)
    else:
        neg_list.append(var)

print('Positive list:', pos_list)
print('Negative list:',neg_list)

# Positive list: [2, 5, 12, 40]
# Negative list: [-10, -7, -25, -40]