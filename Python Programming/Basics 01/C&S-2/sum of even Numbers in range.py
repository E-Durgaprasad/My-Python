"""Description:
Write a program to print sum of all even numbers in between the Given Numbers
Example:
Input : 20
        40
Output :270.
"""
n=int(input("Enter a number:"))
m=int(input("Enter a number"))
sum=0
for i in range(n+1,m):
    if i%2==0:
        sum=sum+i
print(sum,end="")
