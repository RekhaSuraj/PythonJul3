# different datatypes in a dictionary

d1 = {'Name':['Anuhya','Katyayanee','VidyaBhushan'],
      'Age' :(22,23,24),
      'Email':{'abc@gmail.com','xyz@gmail.com','lmn@gmail.com'}
      }

print(type(d1))
# <class 'dict'>
print(d1)
# {'Name': ['Anuhya', 'Katyayanee', 'VidyaBhushan'], 'Age': (22, 23, 24), 'Email': {'xyz@gmail.com', 'lmn@gmail.com', 'abc@gmail.com'}}

# From key fetch values
print(d1['Name'])
# ['Anuhya', 'Katyayanee', 'VidyaBhushan']

print(d1['Age'])
# (22, 23, 24)

print(d1['Email'])
# {'abc@gmail.com', 'lmn@gmail.com', 'xyz@gmail.com'}

# dictionary get method, we can fetch values
print(d1.get('Name'))
# ['Anuhya', 'Katyayanee', 'VidyaBhushan']

# To fetch individual values, we can use indexing
print(d1['Name'][1])
# Katyayanee




