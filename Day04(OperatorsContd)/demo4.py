# Identity operators : It works on iterables (list, tuple,set,dict)
# is, is not

# is - Returns True if address of the objects are same, else False
list1 = [10,20,30]
list2 = [10,20,30]
print(list1 is list2)
# False
# syntax: id(object) - to check address of an object

print(id(list1))
# 2153418772864

print(id(list2))
# 2317302225088

list3 = list1
print(list1 is list3)
# True

print(id(list3))
# 2162491969920

# is not - Return True if both objects are not same or it is not pointing to the same memory location
print(list1 is not list2)
# True

print(list1 is not list3)
# False

a = 10
b = 10
print(a is b)

print(id(a))
print(id(b))
# 140736912767704
# 140736912767704

str1 = 'hello'
str2 = 'hello'

print(str1 is str2)
# True
