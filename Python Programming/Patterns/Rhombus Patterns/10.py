"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
*      *
* *    *
*   *  *
*    * *
*      * """
n=int(input("enter input:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if  j==1 or j==i or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()