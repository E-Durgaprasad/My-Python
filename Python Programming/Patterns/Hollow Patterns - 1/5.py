"""Description:
Write a Program to Print the following Pattern?
If Input is 5 then Print

*
* *
*   *
*     *
* * * * *

"""
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for k in range(1,i+1):
        if i==n or k==i or k==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()