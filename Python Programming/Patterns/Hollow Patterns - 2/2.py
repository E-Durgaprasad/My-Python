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
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        for j in range(1,i):
            print(" ",end="")
        for k in range(1,n+1):
            if i==1 or k==1 or k==n or i==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()