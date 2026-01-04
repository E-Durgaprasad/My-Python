"""Description:
Write a Program to Print the Given Number is Prime or not without using count?
Constraints:
Input          :- First Line of Input Consists of One Integer Value.
Output        :- Print the Prime Number or Not a Prime Number..

Example:
Input 1  :    83
Output 1:    Prime Number"""

import math
n=int(input("Enter the Number : "))
for i in range(2,int(math.sqrt(n)+1)):
    if n % i == 0:
        print("Not Prime Number")
        break
else:
    print("Prime Number")
