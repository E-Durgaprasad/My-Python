"""Write a Program to Print the Following Pattern?
If Input is 5 then Print
    A
   B B
  C C C
 D D D D
E E E E E"""

n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()