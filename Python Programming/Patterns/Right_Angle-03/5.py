"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
1
01
010
1010
10101"""
n=int(input("Enter number: "))
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if c%2==0:
            print(0,end="")
        else:
            print(1,end="")
        c+=1
    print()