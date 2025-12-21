"""Description:
Write a Program to Print the following Basic Pattern?

If Input is 5 then Print

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

n=int(input("Enter number: "))
for i in range(1,n+1):
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end=" ")
        print()