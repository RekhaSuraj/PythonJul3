# Write a python code to check username and password
# username : python
# pwd : 1234
# True - Access Granted
# False - Access Denied

username = input('Please enter your name:')
password = int(input('Please enter password:'))

if username.lower() == 'python' and password == 1234:
    print('Access Granted')
else:
    print('Access Denied')

# Please enter your name:python
# Please enter password:1234
# Access Granted

# Please enter your name:python
# Please enter password:5678
# Access Denied

# Please enter your name:abc
# Please enter password:1234
# Access Denied

# Please enter your name:Python
# Please enter password:1234
# Access Granted