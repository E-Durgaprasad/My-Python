"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
*****
****
***
**
*"""
n=int(input("Enter Number:"))
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print("*",end="")
        print()