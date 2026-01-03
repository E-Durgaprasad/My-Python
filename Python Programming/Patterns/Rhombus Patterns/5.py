"""Description:
Write a Program to Print the Following Pattern?
If Input is 4 then Print
   1
  121
 12321
1234321
 12321
  121
   1  """
n=int(input("Enter the numbers: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for l in range(1,i+1):
        print(l,end="")
    for m in range(1,i):
        print(i-m,end="")
    print()
c=n-2
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for l in range(1,n-i+1):
        print(l,end="")
    for m in range(1,n-i):
        print(c-m+1,end="")
    c-=1
    print()

