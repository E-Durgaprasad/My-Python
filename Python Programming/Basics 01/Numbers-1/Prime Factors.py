"""Description:
Write a program to print all Prime Factors of a Given Number?
Constraints:
Input          :- First Line of Input Consists of One Integer Value.
Output        :- Print All the Prime Factors of a Given Number.

Example:

Input:18
Output 2 3
"""
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
n=int(input("Enter the Number : "))
c=0
for i in range(1,n+1):
    if n%i==0 and prime(i):
        c+=1
        print(i,end=" ")
if c==0:
    print("No Prime Factors")