"""Description:
Write a Program to Print the Following Pattern?
If Input is 4 then Print
   1
  212
 32123
4321234"""
n=int(input("Enter the no of sides: "))
c=1
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(c-k+1,end="")
    c=c+1
    d=2
    for l in range(1,i):
        print(d,end="")
        d=d+1
    print()