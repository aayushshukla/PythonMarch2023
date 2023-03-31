#input(msg) msg is option
# to take input from user
# it will return String
# int(str) to convert numeric string to int
# float(str) , bin(str) to convert numeric string into binary
# list () , dict() , tuple() ,set()
# str() to convert object into string object
name=input('enter your name')
age = int(input('enter age'))
print('welcome user',name)
print(f'{name} age is {age}')
print('data type of age ',type(age))
print(age -10)
