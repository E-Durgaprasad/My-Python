"""Write a Program to Print the Following Pattern?
If Input is 5 then Print
12345
 2345
  345
   45
    5
   45
  345
 2345
12345  """
n=int(input("Enter the number: "))
for i in range(1,n):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n-i+2):
        print(i+k-1,end="")
    print()
g=n
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(g+k-1,end="")
    g-=1
    print()