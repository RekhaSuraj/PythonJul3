s2 = "It is raining"
# count() - Return the number of non-overlapping occurrences of substring
# sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation
# i has occurred 3 times in the above string, note that it is checking for only lower case "i"

print(s2.count("i"))
# 3

new_s = s2.lower()
print(new_s.count("i"))
# 4

print()
# startswith() - Return True if S starts with the specified prefix, False otherwise. With optional start,
# test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a
# tuple of strings to try
print(s2.startswith("i"))
# False

print(s2.startswith("I"))
# True

#hw: s1.istitle()
# s1.swapcase()
# s1.endswith()



