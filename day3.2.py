pa=int(input('enter amount'))
rate =float(input('enter rate of interest'))
yr = float(input('enter the duration'))
si = pa*rate*yr/100
print(f'amount = {pa} rate of interest = {rate} and time = {yr} and si = {si}')


# wap to calculate area of circle , radius will be user input
import math
r=int(input('enter radius '))
print(f'area of circle is = {math.pi*(r**2)}')

# wap to conver temp from celsuis to farenheit
temp=float(input('enter temp in celsuis'))
ftemp=(temp*9/5)+32
print(f'temp {temp} to {ftemp} in farenheit')

#wap to swap two numbers  x= 10  , y=30 by using 3rd variable 
x=int(input('enter no 1'))
y=int(input('enter no 2'))
temp = x
x=y
y=temp
print('values after swap',x,y)

#swap without 3rd variable
x=int(input('enter no 1'))
y=int(input('enter no 2'))
x , y = y, x
print('values after swap',x,y)

