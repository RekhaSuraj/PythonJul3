# Slicing - Fetching a part of the string
# Syntax: [start:stop:step]

# start - From which index we want to extract the string
# stop - Till the index we want to stop. (+1 index)
# step - Jump

str1 = "India is a great Country"

print(len(str1))
# Fetch great from the above string
s1 = str1[11:16]
print(s1)
# great

# If we dont specify start index, it will take dafault 0
s2 = str1[:6]
print(s2)

# If we dont spedify stop index, it will take till last index
s3 = str1[10:]
print(s3)

# If we dont specify start and stop index
s4 = str1[::]
print(s4)
# India is a great Country

# step - Number of jumps, by deafult it is 1
s1 = str1[:10:1]
print(s1)
# India is a

s2 = str1[:10:2]
print(s2)
# Idai 

s3 = str1[::3]
print(s3)
# Iiiartot