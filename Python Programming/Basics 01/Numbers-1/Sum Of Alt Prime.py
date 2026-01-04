"""Description:
Write a program to find the Sum of all Alternative Prime Numbers between The Given Values.
Constraints:
Input          :- First Line of Input Consists of One Integer Value ( Minimum Value ) .
            Second Line of Input Consists of One Integer Value ( Maximum Value ) .
Output        :- Print Sum of All Alternate Prime Numbers Between the Given Values.
Example:
Input 1  :25
          100
Output 1:462

"""
import math
def prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
n=int(input("enter the number:"))
e=int(input("enter the number:"))
alt=0
sum=0
for i in range(n,e+1):
    if prime(i):
        alt=alt+1
        if alt % 2 ==1:
            sum=sum+i
print(sum,end="")
