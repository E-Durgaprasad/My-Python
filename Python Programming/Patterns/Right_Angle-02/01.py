"""Description:
Write a Program to Print the Following Pattern?
If Input is 6 then Print
1 2 3 4 5 6
5 4 3 2 1
1 2 3 4
3 2 1
1 2
1"""

n=int(input("Enter Number:"))
if n<=0:
    print("Invalid Input")
else:
    c=1
    for i in range(1,n+1):
        if i%2==1:
            for j in range(1,n-i+2):
                print(j,end=" ")
        else:
            for j in range(n - i + 1, 0, -1):
                print(j, end=" ")
            c-=1
        print()


