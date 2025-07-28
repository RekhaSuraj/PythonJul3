# Program to reverse a number using while loop
# 12345
# 54321


num = int(input('Please enter a number'))
rev_num = 0

while num != 0:
    rem = num % 10
    rev_num = (rev_num * 10) + rem
    num = num // 10
    print(num)

print(rev_num)

# 1234
# 123
# 12
# 1
# 0
#
# 54321