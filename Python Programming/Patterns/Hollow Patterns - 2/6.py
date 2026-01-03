"""Write a Program to Print the following Hollow Pattern?
If Input is 5 then Print
    *
    *
* * * * *
    *
    *
If Input is 6 then Print
    * *
    * *
* * * * * *
* * * * * *
    * *
    * *

"""
n=int(input("Enter a number: "))

if n%2==1:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==n//2+1 or i==n//2+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==n//2 or i==n//2+1 or j==n//2 or j==n//2+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

