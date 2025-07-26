# range(start, stop, step)
# start is not mandatory - default is 0
# stop is mandatory, stops at -1 from the given stop range
# step - jumps/increments

for var in range(1,11):
    print(var)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# if i dont specify start, it will consider 0 as default start amd the number for stop
for v in range(10):
    print(v,end=" ")

# 0 1 2 3 4 5 6 7 8 9
print()

# step - 2 jumps from 0 returns even numbers
for s in range(0,20,2):
    print(s, end=' ')

# 0 2 4 6 8 10 12 14 16 18

print()
# step - 2 from 1 returns odd numbers
for x in range(1,20,2):
    print(x, end=' ')

# 1 3 5 7 9 11 13 15 17 19

print()
# step : -1 prints in reverse order
for var in range(10,0,-1):
    print(var, end=" ")

# 10 9 8 7 6 5 4 3 2 1