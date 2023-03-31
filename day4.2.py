n = int(input('enter number to check multiple of 10'))
if n%2==0 and n%5==0:
    print(f'{n} is multiple of 10')
else:
    print(f'{n} is not mutiple of 10')



# wap to print grade of student on basis of total marks given by user
# gt 90  - A+, gt 80 lt 90 -A , gt 70 lt 80 -B+ , gt 60 lt 70 B ,gt 50 lt 60 - C, lt 50 failed

tm=int(input('enter total marks'))
if tm>=90 and tm <=100:
    print("A+")
elif tm>=80 and tm<90:
    print("A")
elif tm>=70 and tm<80:
    print("B+")
elif tm>=60 and tm<70:
    print("B")
elif tm>=50 and tm<60:
    print("C")
else:
    print("Fail")
