# Write a program to find out the sum of numbers until user enters 0

num1 = int(input('Please enter a number'))
sum1 = 0
while num1 != 0:
    sum1 = num1 + sum1
    print(sum1)
    num1 = int(input('Please enter another number'))

print(sum1)

# Please enter a number2
# 2
# Please enter another number1
# 3
# Please enter another number1
# 4
# Please enter another number2
# 6
# Please enter another number0
# 6