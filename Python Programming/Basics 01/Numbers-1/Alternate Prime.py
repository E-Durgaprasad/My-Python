"""Write a program to print Alternative Prime Numbers in the Given Range.
Constraints:
Input          :- First Line of Input Consists of One Integer Value ( Minimum Value ) .
                     Second Line of Input Consists of One Integer Value ( Maximum Value ) .
Output        :- Print Alternate Prime Numbers in the Given Range.
Constraints  :- Given Inputs Must be Greater than Zero or else Print "Invalid Inputs".

Example:
Input
1: 25
100
Output
1: 29, 37, 43, 53, 61, 71, 79, 89

"""
import math
def prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
n=int(input("Enter Number : "))
e=int(input("Enter Euclidean Distance : "))
count=0
alt=0
for i in range(n,e+1):
    if prime(i):
        alt = alt + 1
        if alt % 2 == 1:
            count = count + 1
            if count != 1:
                print(", ", end="")
            print(i, end="")