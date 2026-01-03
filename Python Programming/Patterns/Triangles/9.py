"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1 """
n=int(input("Enter the input: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    c=1
    for k in range(1,i+1):
        print(c,end=" ")
        c = c * (i - k) // k
    print()

