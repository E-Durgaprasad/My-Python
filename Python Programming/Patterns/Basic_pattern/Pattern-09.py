"""Description:
Write a Program to Print the following Basic Pattern?
If Input is 5 then Print
55555
54444
54333
54322
54321"""
n=int(input("Enter Number:"))
if n==0:
    print("InvaliD Input")
else:
    if n<0:
        n=abs(n)
        c=0
    for i in range(1,n+1):
        c=n
        for j in range(1,i):
            print(c,end="")
            c-=1
        for k in range(1,n-i+2):
            print(c,end="")
        print()