"""Description.:
Write a program to print all alternative even numbers
in the given range if no numbers then print NO NUMBERS
if starting range is greater than ending range print INVALID INPUTS
Example:
Input: 10
        30
output: 10 14 18 22 26 30
"""
n=int(input("Enter a number:"))
m=int(input("Enter a number:"))
c=0
for i in range(n,m+1):
    if i%2==0:
        c+=1
        if c%2!=0:
            print(i,end=" ")