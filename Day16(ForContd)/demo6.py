# Print only doses in a separate list
l1 = ['Masala dose','Rava Dose','Idly','Onion Dose','Pongal','Upma','Plain Dose']

dose_list = []
for var in l1:
    if 'dose' in var.lower():
        dose_list.append(var)


print(dose_list)
# ['Masala dose', 'Rava Dose', 'Onion Dose', 'Plain Dose']


# Find the biggest number in a list without using max() inbuilt method
list1 = [4,10,15,45,20,7,25,30]

big = list1[0]
for i in list1:
    if i > big:
        big = i

print(big)

# 45
# inbuilt method max()
print(max(list1))
# 45

# hw - find the smallest number in a list without using min() inbuilt method
list2 = [30,45,5,15,20,1,4]

print()