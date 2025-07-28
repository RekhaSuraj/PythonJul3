# Print first 7 numbers which are divisible by 7 and 8

i = 0
cntr = 0
while cntr <= 6:
    if i % 7 == 0 and i % 8 == 0:
        print(i)
        cntr += 1

    i += 1

# 0
# 56
# 112
# 168
# 224
# 280
# 336


