"""Description:
Write a Program to Print the following Hollow Pattern?
If Input is 4 then Print

*     *
 *   *
  * *
   *
  * *
 *   *
*     *

"""
n=int(input("Enter a number: "))
for i in range(1,n):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n-i+2):
        if k==1 or k==n-i+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        if k==1 or i==k:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()