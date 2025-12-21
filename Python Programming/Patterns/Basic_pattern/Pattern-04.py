"""Write a Program to Print the following Basic Pattern?
If Input is 5 then Print
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
n=int(input("Enter Number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()