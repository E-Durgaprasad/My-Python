"""Write a Program to Print the Following Pattern?
If Input is 7 then Print
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7"""
n=int(input("Enter Number:"))
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()