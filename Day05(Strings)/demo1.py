# string - Inside single quotes or double quotes
str1 = 'welcome'
print(type(str1))

str2 = "Hello"
print(type(str2))

# <class 'str'>
# <class 'str'>

# Empty string
s = ""

print(type(s))
# <class 'str'>

# Concatenation of strings - Joining of 2 or more strings + operator

s1 = "Python "
s2 = 'Developer'

s3 = s1 + s2
print(s3)
# Python Developer

# Printing in a new line - "\n"
a = "Hello"
b = "World"

print(a + "\n" + b)
# Hello
# World


# Print a string multiple times - repeatition
str1 = "Welcome to GRK"

print(str1 * 4)
# Welcome to GRKWelcome to GRKWelcome to GRKWelcome to GRK
print("Welcome to GRK\n"*4)

# Welcome to GRK
# Welcome to GRK
# Welcome to GRK
# Welcome to GRK


# String and a variable in the same line

n1 = 10
n2 = 20
n3 = n1 + n2
print("Addition of n1 and n2 is:",n3)
# Addition of n1 and n2 is: 30

print(f'Addition of {n1} and {n2} is {n3}')
# Addition of 10 and 20 is 30






