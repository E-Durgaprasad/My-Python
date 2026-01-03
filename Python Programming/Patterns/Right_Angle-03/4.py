"""Write a Program to Print the Following Pattern?
If Input is 7 then Print
            G
          G F
        G F E
      G F E D
    G F E D C
  G F E D C B
G F E D C B A"""
n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(i):
        print(chr(64+n-k),end=" ")
    print()