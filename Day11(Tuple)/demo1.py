# Tuple - Is an inbuilt datatype in python
# It is used to store multiple values within a single unit to assign to a variable name
# Tuple is denoted by round braces / Paranthesis ()
# Tuples are immutable - Cannot be modified once created
# Tuples can be homogeneous or heterogeneous

# Method 1 to create a tuple
t1 = (10,20,30,40,50)
print(type(t1))
# <class 'tuple'>


# Method 2 - Using constructor
t2 = tuple((25,35,'hi',54.5,4+5j,'hello'))
print(type(t2))
# <class 'tuple'>
print(t2)
# (25, 35, 'hi', 54.5, (4+5j), 'hello')

# Tuple supports indexing
print(t2[3])
# 54.5

# Create an empty tuple
t3 = ()
print(type(t3))
# <class 'tuple'>
print(t3)

