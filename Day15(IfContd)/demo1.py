# if elif elif... else condition

# Chain multiple if statements in python
# We check multiple conditions one after the other

# syntax:
# if condition 1:
#     statement 1
# elif condition 2:
#     statement 2
# elif condition 3:
#      statement 3
#      ...

# else
#      statement

# In the above example, the elif conditions are applied after the if condition
# Here if one elif condition is satisfied, it skips the next elif conditions and comes out of the if block
# completely

num1 = int(input('Please enter a number'))
if num1 == 1:
    print('Sunday')
elif num1 == 2:
    print('Monday')
elif num1 == 3:
    print('Tuesday')
elif num1 == 4:
    print('Wednesday')
elif num1 == 5:
    print('Thursday')
elif num1 == 6:
    print('Friday')
elif num1 == 7:
    print('Saturday')
else:
    print('Invalid Input')

# Please enter a number2
# Monday

# Please enter a number7
# Saturday

# Please enter a number8
# Invalid Input






