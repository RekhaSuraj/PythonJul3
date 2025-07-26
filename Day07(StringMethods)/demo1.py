# String Methods - Immutable, modify a string, we can only assign it to a different string
# print(help(str))

# upper() - Return a copy of the string converted to uppercase(capital letter)
str1 = "Today is a Good Day"
# print(str1.upper())
# TODAY IS A GOOD DAY
res = str1.upper()
print(res)
# TODAY IS A GOOD DAY



# lower() - Return a copy of the string converted to lowercase(small letter)
str_low = str1.lower()
print(str_low)
# today is a good day

# casefold() - Return a version of the string suitable for caseless comparisons
# This method is a more aggressive form of lowercasing, designed for caseless matching and
# comparisons across various languages and Unicode characters.
# It removes all case distinctions, including those that lower() might miss

s1 = "ß"
print(s1.casefold())
print(s1.lower())
# ss
# ß