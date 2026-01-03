"""Write a Program to Print the Following Pattern?
If Input is 4 then Print
4444444
 33333
  222
   1  """
n=int(input("Enter the input: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n-i+2):
        print(n-i+1,end="")
    for l in range(1,n-i+1):
        print(n-i+1,end="")
    print()