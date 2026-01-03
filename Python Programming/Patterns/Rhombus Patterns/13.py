"""Write a Program to Print the Following Pattern?
If Input is 5 then Print
    *
   # #
  * * *
 # # # #
* * * * *
 # # # #
  * * *
   # #
    *
"""
n=int(input("Enter the number: "))
if n%2==1:
        for i in range(1,n+1):
            for j in range(1,n-i+1):
                print(" ",end="")
            for k in range(1,i+1):
                if i%2==1:
                    print("*",end=" ")
                else:
                    print("#",end=" ")
            print()
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(" ",end="")
            for k in range(1,n-i+1):
                if i%2==0:
                    print("*",end=" ")
                else:
                    print("#",end=" ")
            print()
else:
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ",end="")
        for k in range(1,i+1):
            if i%2==1:
                print("*",end=" ")
            else:
                print("#",end=" ")
        print()
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(" ",end="")
        for k in range(1,n-i+1):
            if i%2==0:
                print("#",end=" ")
            else:
                print("*",end=" ")
        print()