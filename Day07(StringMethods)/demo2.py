s1 = "welcome to gRK"
# capitalize() - Return a capitalized version of the string.
# More specifically, make the first character have upper case and the rest lower case
print(s1.capitalize())
# Welcome to grk

# Return a version of the string where each word is titlecased.
# More specifically, words start with uppercased characters and all remaining cased
# characters have lower case.
print(s1.title())
# Welcome To Grk

# isupper() - Return True if the string is an uppercase string, False otherwise.
# A string is uppercase if all cased characters in the string are uppercase and there is at least
# one cased character in the string
print(s1.isupper())
# False

str1 = 'HOW ARE YOU?'
print(str1.isupper())
# True

# Return True if the string is a lowercase string, False otherwise.
# A string is lowercase if all cased characters in the string are lowercase and there is at least
# one cased character in the string.
print(s1.islower())
# False

# isnumeric()
# Return True if the string is a numeric string, False otherwise.
# A string is numeric if all characters in the string are numeric and there is at least one character
# in the string

# str2 = "12345"
# str2 = "¼"
# str2 = "ⅠⅢⅧ"
str2 = "१२३"
print(str2.isnumeric())
# True

# Return True if the string is a digit string, False otherwise.
# A string is a digit string if all characters in the string are digits and there is at least
# one character in the string.
print(str2.isdigit())

