"""Description:
Write a Program to Print the following Basic Pattern?
If Input is 5 then Print
1 0 0 0 0
0 2 0 0 0
0 0 3 0 0
0 0 0 4 0
0 0 0 0 5"""

n=int(input("Enter a Number:"))
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                print(i,end=" ")
            else:
                print("0",end=" ")
        print()