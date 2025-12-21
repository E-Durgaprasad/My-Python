"""Description:
Write a Program to Print the following Basic Pattern?
If Input is 6 then Print
1 1 1 1 1 1
1 1 1 1 2 2
1 1 1 3 3 3
1 1 4 4 4 4
1 5 5 5 5 5
6 6 6 6 6 6"""

n=int(input("Enter Number:"))
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        for j in range(1,n-i+1):
                print(1,end=" ")
        for k in range(1,i+1):
            print(i,end=" ")
        print()