"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15"""

n=int(input("Enter a number: "))
for i in range(1,n+1):
    c=i
    for j in range(1,i+1):
            print(c,end=" ")
            c=c+n-j
    print()