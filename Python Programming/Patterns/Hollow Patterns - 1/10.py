"""Description:
Write a Program to Print the following Hollow Pattern?
If Input is 5 then Print

* * * * *
*     *
*   *
* *
*

"""
n=int(input("Enter the no.: "))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        if j==1 or i==1 or j==n-i+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
