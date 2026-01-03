"""Description:
Write a Program to Print the Following Pattern?
If Input is 4 and 5 then Print
5 @ 5 – odd
7 9 @ 16 – even
11 13 15 @ 39 – odd
17 19 21 23 @ 80 – even"""

n=int(input("Enter Numbers: "))
m=int(input("Enter Numbers: "))
if n<=0 or m<=0:
    print("Invalid Input")
else:
    c=m
    for i in range(1,n+1):
        sum = 0
        for j in range(1,i+1):
            print(c,end=" ")
            sum=sum+c
            c+=2
        print(f"@",sum,"-",end="")
        if i%2==0:
            print("even")
        else:
            print("odd")
        print()
