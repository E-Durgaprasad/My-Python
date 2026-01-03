"""Description:
Write a Program to Print the following Basic Pattern?
If Input is 4 then Print

01 02 03 04
05       06
07       08
09 10 11 12

"""
n=int(input("Enter the number: "))
c=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or j==n or i==n:
            if c<10:
                print(f"0{c}",end=" ")
            else:
                print(c,end=" ")
            c+=1
        else:
            print(" ",end="  ")
    print()
