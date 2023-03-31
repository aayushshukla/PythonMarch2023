n = int(input('enter number ')) #1234
r1= n%10 # 4
q1=n//10 #123
r2= q1%10 #3
q2=q1//10  #12
r3=q2%10 # 2
q3=q2//10  # 1
print(r1,r2,r3,q3)

#gst
noi = int(input('enter number of items'))
poi=float(input('enter price of item'))
gst=float(input('enter gst '))
totalbill= (noi*poi) + (noi*poi*gst)/100
print('No of items =',noi)
print('Price of item =',poi)
print('GST % is =',gst)
print('Amount is =',(noi*poi))
print('GST amount = ',(noi*poi*gst)/100)
print('total bill',totalbill)
