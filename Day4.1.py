pin =1234
upin =int(input('enter your pin'))
amt =10000
if pin == upin:
    print('Enter 1 to withdraw')
    print('Enter 2 to deposite')
    print('Enter 3 to check balance')
    print('Enter 4 to exit')
    ch=int(input('Enter the operation you want to perform'))
    if ch==1:
        wamt = int(input('Enter amount to withdraw'))
        if wamt<=amt:
            if wamt%100==0:
                if wamt>=100:
                    #amt=amt-wamt
                    amt -= wamt
                    print('----Receipt---- \n')
                    print('Amount Withdraw',wamt)
                    print('Balance Amount',amt)
                else:
                    print('Invalid amount ')
            else:
                print('Amount should be multiple of 100 , 200 or 500')
        else:
            print('Insufficient Balance')
    elif ch==2:
        pass
    elif ch==3:
        print('Balance is ',amt)
    elif ch==4:
        exit(1)
    else:
        print('Invalid option selected')

else:
    print('Invalid pin')
