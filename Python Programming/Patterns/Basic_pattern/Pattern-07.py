"""Description:
Write a Program to Print the following Basic Pattern?
If Input is 5 and 6 then Print
* * * * * *
* $ $ $ $ *
* $ $ $ $ *
* $ $ $ $ *
* * * * * *"""

r,c=map(int,input("Enter Number:").split())
if r<=0 or c<=0:
    print("Invalid Inputs")
else:
    for i in range(1,r+1):
        for j in range(1,c+1):
            if i==1 or i==r or j==1 or j==c:
               print("*",end=" ")
            else:
                print("$",end=" ")
        print()