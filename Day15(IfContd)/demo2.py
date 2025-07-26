# Check for positive or negative or zero from user
num1 = int(input('Please enter a number'))

if num1 > 0:
    print(f'{num1} is Positive number')
elif num1 < 0:
    print(f'{num1} is Negative number')
elif num1 == 0:
    print(f'{num1} is zero')
else:
    print('Invalid input')

# Please enter a number4
# 4 is Positive number

# Please enter a number-5
# -5 is Negative number

# Please enter a number0
# 0 is zero