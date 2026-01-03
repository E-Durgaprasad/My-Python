"""Description:
Write a Program to Print the following Hollow Pattern?
If Input is 5 then Print

* * * * *
 *     *
  *   *
   * *
    *

"""
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n-i+2):
        print("*",end=" ")
    print()