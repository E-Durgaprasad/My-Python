"""Description:
Write a Program to Print the Following Pattern?
If Input is 4 then Print
   0
  0 0
 0 0 0
0 0 0 0
 0 0 0
  0 0
   0  """
n=int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("0",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,n-i+1):
        print("0",end=" ")
    print()