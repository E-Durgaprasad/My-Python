"""Write a Program to Print the following Hollow Pattern?
If Input is 5 then Print

*
* *
*  *
*   *
*    *
*   *
*  *
* *
*

"""
n=int(input("Enter the number: "))
for i in range(1,n):
    for j in range(1,i+1):
        if j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()
for i in range(1,n+1):
    for j in range(1,n-i+2):
        if j==n-i+1 or j==1:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()
