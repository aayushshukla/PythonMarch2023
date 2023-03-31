idtype =input("enter PAN for pancard , ADHAAR for adhaar card")
if idtype == 'PAN' or idtype == 'ADHAAR':
    idno=input('enter your id no')
    if idno.isnumeric():
        if len(idno)==12:
            print(" Thank you for sharing your adhaar detail")
            print(f'{idtype} no is {idno} ')
        else:
            print('Invalid adhaar no')
    else:
        print(" Thank you for sharing your pan card detail")
        print(f'{idtype} no is {idno} ')
else:
    print("Only adhaar and pancard is supported ")
