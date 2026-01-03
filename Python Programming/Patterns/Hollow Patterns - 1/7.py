"""Description:
Write a Program to Print the following Hollow Pattern?
If Input is 5 then Print
* * * * *
*       *
*       *
*       *
* * * * *
"""
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or i==1 or j==n or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

