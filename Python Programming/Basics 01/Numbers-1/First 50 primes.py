"""Write a Program to print the first 50 prime Numbers without using Factors count?
Constraints:
Input          :- First Line of Input Consists of One Integer Value ( N ) .
Output        :- Print First N no of Prime Numbers..

Example:
Input 1  :    16

Output 1:    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53

"""
import math
def prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
n=int(input("Enter Number:"))
c=0
pn=2
while c<n:
    if prime(pn):
        c+=1
        if c!=1:
            print(",",end="")
        print(pn,end="")
    pn+=1