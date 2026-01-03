"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
            01
         02 03
      04 05 06
   07 08 09 10
11 12 13 14 15"""
n=int(input("Enter Number: "))
c=1
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("  ",end=" ")
    for k in range(1,i+1):
        if c<10:
            print(f"0{c}",end=" ")
        else:
            print(f"{c}",end=" ")
        c+=1
    print()