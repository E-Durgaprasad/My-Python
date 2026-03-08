# Write a program to Find Sum of Digits of a Given Number?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print Sum of Digits as Given in Examples.
# Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input.".
# Example:
# Input 1  :    25696
# Output 1:    2 + 5 + 6 + 9 + 6.
n=int(input("Enter Number:"))
count=0
s=0
a=0
if n<=0:
    print("Invalid Input.")
else:
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    while s>0:
        r=s%10
        a=a*10+r
        s=s//10
        count+=1
        if count!=1:
            print(" + ",end="")
        print(r,end="")
    print(".")

