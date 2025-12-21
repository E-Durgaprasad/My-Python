"""Description:
Write a Program to Print the following Basic Pattern?
If Input is 3 and 5 then Print
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
Constraints:
Input          :- First Line of Input Consists of Two Integer Values ( Rows & Columns ).
Output        :- Print the Following Pattern.
Constraints  :- Either of the Given Inputs is Zero then Print Invalid Inputs
        If the Given Inputs is Negative then Convert into Positive and then Print Following Output"""

r,c=map(int,input("Enter Number:").split())
if r==0 or c==0:
    print("Invalid Inputs")
else:
    r=abs(r)
    c=abs(c)
    co=1
    for i in range (1,r+1):
        for j in range(1,c+1):
            print(co,end=" ")
            co+=1
        print()