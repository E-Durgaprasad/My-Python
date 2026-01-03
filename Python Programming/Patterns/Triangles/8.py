"""Description:
Write a Program to Print the Following Pattern?
If Input is 4 then Print
   1
  121
 12321
1234321 """
n=int(input("Enter the inputs: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    for l in range(1,i):
        print(i-l,end="")
    print()
