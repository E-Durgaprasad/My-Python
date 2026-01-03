"""Description:
Write a Program to Print the Following Pattern?
If Input is 4 then Print
   1
  1 2
 1 2 3
1 2 3 4"""
n=int(input("Enter the inputs: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()