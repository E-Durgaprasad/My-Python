"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5"""
n=int(input("Enter Number: "))
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        c = n
        for j in range(1,n-i+2):
            print(c,end=" ")
            c-=1
        print()

