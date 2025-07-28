# Print first 5 even numbers

i = 0
even_cntr = 0
while even_cntr <= 4:
    if i % 2 == 0:
        print(i)
        even_cntr += 1
        # print(even_cntr)
    i += 1

# 0
# 2
# 4
# 6
# 8

# hw - print first 10 odd numbers