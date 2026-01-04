"""Description:

Write a program to print All the Prime Numbers in the Given Range.
Constraints:
Input :- First Line of Input Consists of One Integer Value ( Minimum Value ) .
        Second Line of Input Consists of One Integer Value ( Maximum Value ) .
Output :- Print All the Prime Numbers in the Given Range.

Example:

Input
1: 25
100
Output
1: 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
"""
import math
def prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
n=int(input("Enter number: "))
e=int(input("Enter the Euclidean Distance: "))
c=0
for i in range(n,e+1):
    if prime(i):
        c+=1
        if c!=1:
            print(",",end="")
        print(i,end="")
