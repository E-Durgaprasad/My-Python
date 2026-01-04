"""Description:
Write a program to print all factors of the Given Number.
Constraints:
Input          :- First Line of Input Consists of One Integer Value.
Output        :- Print All the Factors of the Given Number.
Constraints  :- Given Input Must be Greater than Zero or else Print "Invalid Input".

Example:
Input 1  :    18
Output 1:    1 2 3 6 9 18
"""
n=int(input("Enter Number: "))
for i in range(1,n+1):
    if n % i == 0:
        print(i,end=" ")