"""Description:
Write a Program to Print the following Basic Pattern?
If Input is 5 and 5 then Print
1*2*3*4*5
6*7*8*9*10
11*12*13*14*15
16*17*18*19*20
21*22*23*24*25

Constraints:
Input          :- First Line of Input Consists of Two Integer Values ( Rows & Columns ).
Output        :- Print the Given Pattern.
Constraints  :- Given Inputs Must be Greater than Zero ->Print the following Pattern.
-->If the Given Inputs: Row and Column values are less than or equal to Zero then Print Invalid Row and Column Values
-->If the Given Inputs: Row value is less than or equal to Zero then Print Invalid Row Value.
-->If the Given Inputs: Column value is less than or equal to Zero then Print Invalid Column Value."""

r,c=map(int,input("Enter Numbers:").split())
num=1
if r<=0 and c<=0:
    print("Invalid Row and Column Values")
elif r<=0:
    print("Invalid Row Value")
elif c<=0:
    print("Invalid Column Value")
else:
    for i in range(1,r+1):
        count=0
        for j in range(1,c+1):
            count+=1
            if count!=1:
                print("*",end="")
            print(num,end="")
            num+=1
        print()