"""Description:
Write a Program to Print the following Basic Pattern?
If Input is 5 then Print
1 2 3 * 5
6 7 * 9 10
11 * 13 14 15
* 17 18 19 *
21 22 23 * 25"""

n=int(input("Enter a number:"))
if n<=0:
    print("Given Value is Invalid")
else:
    c=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if c%4==0:
                print("*",end=" ")
            else:
                print(c,end=" ")
            c+=1
        print()
