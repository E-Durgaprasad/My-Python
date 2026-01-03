"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
1 2 3 4 5
  2 3 4 5
    3 4 5
      4 5
        5"""
n=int(input("Enter number: "))
for i in range(1,n+1):
    c=i
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(1,n-i+2):
        print(c,end=" ")
        c+=1
    print()