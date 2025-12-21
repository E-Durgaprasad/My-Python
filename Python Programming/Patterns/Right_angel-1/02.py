"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15"""
n=int(input("Enter Number:"))
if n<=0:
    print("Invalid Input")
else:
    c=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(c,end=" ")
            c+=1
        print()