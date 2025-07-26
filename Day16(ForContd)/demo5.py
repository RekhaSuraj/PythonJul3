# Factorial of a number
# 5 factorial - 5*4*3*2*1

n = int(input('Enter number to find factorial'))

fact = 1
for var in range(1, 6):
    fact = fact * var
    print(fact)

print(f'Factorial of {n} is {fact}')

# 1
# 2
# 6
# 24
# 120
# Factorial of 5 is 120