# Description:
# Write a program to print the Sum of all Alternative Palindrome Numbers Between the Given Numbers?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the Sum of All Alternative Palindromes Between the Given Numbers.
# Constraints  :- If Either of the Given Inputs is equal to Zero then, Print "Invalid Inputs".
#                      If there are no Palindrome values between the Given Numbers then, Print "No Palindrome Values".
#                      If Either of the Given Inputs is Negative, then convert those Negative Values to Positive Values.
# Example:
# Input 1  :    100
#                   200
# Output 1:    Sum of Alternative Palindrome Numbers between the 100 and 200 is 101 + 121 + 141 + 161 + 181 = 705.
def pal(i):
    rev=0
    t=i
    while t>0:
        r=t%10
        rev=rev*10+r
        t=t//10
    return i==rev
n=int(input("Enter Number:"))
m=int(input("Enter Number:"))
if n==0 or m==0:
    print("Invalid Inputs")
else:
    if n<0:
        n=abs(n)
    if m<0:
        m=abs(m)
    if n>m:
        n,m=m,n
    sum=0
    count=0
    for i in range(n+1,m):
        if pal(i):
            count+=1
            if count%2==1:
                sum=sum+i
                if count==1:
                    print(f"Sum of Alternative Palindrome Numbers between the {n} and {m} is ",end = "")
                if count!=1:
                    print(" + ",end="")
                print(i,end="")
    if count==0:
        print("No Palindrome Values")
    else:
        print(f" = {sum}.",end="")