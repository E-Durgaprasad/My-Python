"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
10 10 10 10 10
8 8 8 8
6 6 6
4 4
2"""
n=int(input("Enter Number:"))
if n<=0:
    print("Invalid Input")
else:
    c=n*2
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(c,end=" ")
        c=c-2
        print()