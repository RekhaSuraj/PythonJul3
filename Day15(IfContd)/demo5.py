# Looping statements - for loop

# In Python, the for loop is used to iterate over a sequence such as a list, string, tuple,
# other iterable objects such as range.
#
# With the help of for loop, we can iterate over each item present in the sequence and
# execute the same set of operations for each item.
# Using a for loops in Python we can automate and repeat tasks in an efficient manner.
#
# So the bottom line is using the for loop we can repeat the block of statements a fixed number
# of times.
# for loop :
# Iterables : list,string,tuple,set,dict,range,array

# default start value is 0
# range(start=num,stop=num,step=1)
x = range(1,11)
print(type(x))
# <class 'range'>
print(x)
# range(1, 11)

# syntax : for var in iterable:
#               body of for loop


list1 = [10,20,30,40,50,60,70]
for var in list1:
    print(var)

# 10
# 20
# 30
# 40
# 50
# 60
# 70

print()
# Add 1 to every item in the above list
for v in list1:
    print(v+1)

# 11
# 21
# 31
# 41
# 51
# 61
# 71

print()
# print items next to each other
for v1 in list1:
    print(v1, end=' ')

# 10 20 30 40 50 60 70

