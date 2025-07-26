# Nested if-else statements
# In python, nested if-else statements: is an if statement inside another if statement
# Indentation is the only way tp differentiate the level of nesting

# syntax:
# if outer_condition:
#   if inner_condition:
#       statement of inner if
#   else:
#       statement of inner else
# else:
#     outer else
# statement outside of if block

# check for even and odd
num = int(input('Please enter a number'))
if num > 0:
    if num % 2 == 0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an odd number')
else:
    print('Invalid input')

# Please enter a number0
# Invalid input

# Please enter a number3
# 3 is an odd number

# Please enter a number8
# 8 is an even number