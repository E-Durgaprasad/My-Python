"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
5
454
34543
2345432
123454321
2345432
34543
454
5
"""
n=int(input("enter input:"))
for i in range(1,n+1):
        c=i
        for j in range(1,i+1):
            print(n-i+j,end="")
        for k in range(1,i):
            print(n-k,end="")
        print()
for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(i+j,end="")
        for k in range(1,n-i):
            print(n-k,end="")
        print()