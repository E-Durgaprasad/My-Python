"""Write a Program to Print the Following Pattern?
If Input is 5 then Print
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1   """
num = int(input("Enter a number: "))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(i,end=" ")
    print()
for i in range(1,num+1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,num-i+1):
        print(num-i,end=" ")
    print()