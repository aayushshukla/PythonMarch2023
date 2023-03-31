#wap to check a number is even or odd
n=int(input('enter number'))
if n%2==0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')


# amt , wamt   wamt should be less than or equal to amt
# if it is true than show balance amt and withdraw amt
#if it is not true than show insufficient balance

amt=int(input('enter amout'))
wamt=int(input('enter withdraw amount'))
if amt>=wamt:
    amt=amt-wamt
    print('withdraw amount =',wamt)
    print('balance amount =',amt)
else:
    print('insufficient funds')

# check wamt should be multiple of 100

if wamt%100==0:
    amt=amt-wamt
    print('withdraw amount =',wamt)
    print('balance amount =',amt)
else:
    print('withdraw amount should be multiple of 100')
    
