# -ve slicing
s1 = "Python is a high level programming language"
# syntax: [start:stop:step]
# Fetch language using -ve slicing

# start index should always be lesser than stop index 
s2 = s1[-8:-1]
print(s2)
# languag

print(s1[-8:])
# language

# empty string will be the output
print(s1[-8:0])

# if start index is greater than stop index, we will get an empty string
print(s1[-3:-10])

print(s1[-15::2])
# amn agae

