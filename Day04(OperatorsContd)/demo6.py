# Bitwise operators - Binary
# Bitwise and (&)
# Bitwise or (|)
# Bitwise XOR (^)
# Bitwise Not (~)
# Bitwise Shiftleft (<<)
# Bitwise Shiftright(>>)

# Bitwise and (&) - ampersand
a = 5
b = 7

print(a & b)
# 5

# 5 -->0 1 0 1
# 7 -->0 1 1 1
# ----------
# 5 -->0 1 0 1

# Bitwise or (|) - pipe
x = 5
y = 8
print(5 | 8)
# 13


# Bitwise XOR (^) - cap
# Returns False if both values are same(0 or 1), else True
print(5 ^ 7)
# 2



# Bitwise Not(~) - Tilde

a = 10
print(~a)

# Explanation
# Adds one (1) to the value and returns negative value of that
# a = 10
# a = 10 + 1
# a = -(11)

print(~56)
# -57

print(~-46)
# -(-46+1)
# 45
# 45


# Bitwise shiftleft(<<) - Shifts the position of the binary to left (according to the number of positions given)
# This adds the value
a = 5
print('shift left',a << 1)
# 10

# 5 -->0 1 0 1
# << 1
# -----------------
# 10-->1 0 1 0

# Bitwise shiftright (>>) - Shifts the position of binary to right(according to the number of positions given)
# This looses the bits
b = 5
print('shift right',b >> 1)
# 2

# 5 --> 0 1 0 1
# >> 1
# ----------------
# 2 --> 0 0 1 0

