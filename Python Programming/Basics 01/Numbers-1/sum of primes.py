"""Description:
Write a program to find Sum of all the prime numbers between the Given values.
Constraints:
Input          :- First Line of Input Consists of One Integer Value ( Minimum Value ) .
                     Second Line of Input Consists of One Integer Value ( Maximum Value ) .
Output        :- Print Sum of Prime Numbers Between the Given Values.

Example:
Input 1  :    25
Input 2  :    100
Output :    960

"""
import math
def prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
n=int(input("Enter Number:"))
e=int(input("Enter Euclidean Distance:"))
sum=0
for i in range(n,e+1):
    if prime(i):
        sum=sum+i
print(sum)