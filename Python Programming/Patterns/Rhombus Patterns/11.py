"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print

1 2 3 4 5 4 3 2 1
  2 3 4 5 4 3 2
    3 4 5 4 3
      4 5 4
        5
      4 5 4
    3 4 5 4 3
  2 3 4 5 4 3 2
1 2 3 4 5 4 3 2 1

"""
n=int(input("Enter the number: "))
for i in range(1,n):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n-i+2):
        print(i+k-1,end="")
    for l in range(1,n-i+1):
        print(n-l,end="")
    print()
c=n
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(c+k-1,end="")
    c-=1
    g=n
    for l in range(1,i):
        print(g-l,end="")
    print()
