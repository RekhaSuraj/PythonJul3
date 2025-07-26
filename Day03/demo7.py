# Logical Operators : Threee reserved keywords: and, or, not

# and operator
# syntax : x and y
# When x and y are True, it returns True 
# When anyone value is False, it returns False

print(True and True)
# True

print(True and False)
# False

print(False and True)
# False

print(False and False)
# False

# It returns the last truthly value
print(6 and 5)

print('-------------OR Operator----------------')
# or operator
# syntax : a or b
# When atleast one value is True, it returns True
# When both values are False, it returns False

print(True or True)
# True

print(True or False)
# True

print(False or True)
# True

print(False or False)
# False

# It returns the first truthly value
print(6 or 5)
# 6

# In python, these are by defaultly False
# [], (),{},'',0,False - False
print([] and 12)
# []

print(() or 10)
# 10

print('-----not operator ---------')
# not operator - It gives the opposite of the result of operators
# syntax: not(True or False)
# First evaluate the inner braces
print(not(True or True))
# False

print(not(True or False))
# False

print(not(True and False))
# True
