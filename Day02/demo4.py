# Explicit typecasting
# Convert from int to float
a = 20
print('Before conversion',a)
f = float(a)
print('After conversion',f)

# Before conversion 20
# After conversion 20.0


# Convert from float to int
print()
b = 5.2
print('Before conversion',b)
i = int(b)
print('After conversion',i)

# Before conversion 5.2
# After conversion 5
print()

# Convert from string to bool

s = 'True'
print(type(s))
# <class 'str'>
print('Before conversion',s)
b = bool(s)
print('After conversion',b)
print(type(b))

# <class 'str'>
# Before conversion True
# After conversion True
# <class 'bool'>