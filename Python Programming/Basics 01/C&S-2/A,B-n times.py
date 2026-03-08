"""Description:
Write a program to print A,B in given number of times alternatively
Input :          First line of input contains Integer n
Output :       Print A,B for n no of times
Example:
Input :          5
Output :       A,B,A,B,A,B,A,B,A,B
"""
n=int(input("Enter a number:"))
c=0
for i in range(1,n+1):
    c+=1
    if c!=1:
        print(",",end="")
    print("A,B",end="")