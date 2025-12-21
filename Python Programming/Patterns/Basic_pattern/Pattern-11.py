"""Description:
Write a Program to Print the following Basic Pattern?
If Input is 5 4 then Print
* * * *
* * * *
* * * *
* * * *
* * * *"""
r,c=map(int,input("Enter Numbers:").split())
if r<0 or c<0:
    print("Invalid Inputs")
else:
    num=1
    for i in range(1,r+1):
        for j in range(1,c+1):
            print("*",end=" ")
            num+=1
        print()