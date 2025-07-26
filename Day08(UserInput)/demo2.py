# replace
# Return a copy with all occurrences of substring old replaced by new
s1 = "Hello World"
s2 = s1.replace(" ","@")
print(s2)
# Hello@World
print(s1.replace(" ","-"))
# Hello-World

# split() - Return a list of the substrings in the string, using sep as the separator string.
s3 = s1.split()
print(s3)
# ['Hello', 'World']

str1 = "He-llo-Wor-ld"
s4 = str1.split("-")
print(s4)
# ['He', 'llo', 'Wor', 'ld']

s5 = "Hello"
print(s5.split())
# ['Hello']

# print(s5.split(""))
# ValueError: empty separator

print(s5.split(" "))
# ['Hello']

print(list(s5))
# ['H', 'e', 'l', 'l', 'o']

s6 = s5.split()
print(s6)
# ['Hello']

s7 = " ".join(s5)
print(s7)

s8 = s7.split(" ")
print(s8)
# ['H', 'e', 'l', 'l', 'o']