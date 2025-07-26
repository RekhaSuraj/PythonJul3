s1 = "What about thais?"
# index() - Return the lowest index in S where substring sub is found,
# such that sub is contained within S[start:end]. Optional arguments start and end are
# interpreted as in slice notation.
res = s1.index("a")
print(res)
# 2

# We can specify start index like below
print(s1.index("a",3))
# 5
print(s1.index("a",res+1))
# 5

# Also stop index
# print(s1.index("a",6,11))
# ValueError: substring not found

print()
# find() - Return the lowest index in S where substring sub is found, such that sub is contained within
# S[start:end]. Optional arguments start and end are interpreted as in slice notation
print(s1.find("a"))
# 2

print(s1.find("a",3))
# 5

# If the substring is not found, find() gives -1 and does not throw error (Difference between index() and find())
print(s1.find("a",6,11))
# -1

