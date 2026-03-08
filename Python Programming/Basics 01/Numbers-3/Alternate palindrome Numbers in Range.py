# Write a program to print Alternative Palindrome Numbers in the Given Range?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
#
# Output        :- Print the Alternative Palindromes in a Given Range.
# Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "InvAlid InPUts".
#                      If there are no Palindrome values in the Given Range then, Print "No Palindrome Values"
# Example:
# Input
# 1: 100
# 200
# Output
# 1:
# 101, 121, 141, 161, 181

n=int(input("Enter Number:"))
m=int(input("Enter Number:"))
def is_pal(i):
    t=i
    rev=0
    while t>0:
        r=t%10
        rev=rev*10+r
        t=t//10
    return(i==rev)
c=0
if n<0 or m<0:
    print("InvAlid InPUts")
else:
    for i in range(n,m+1):
        if is_pal(i):
            c=c+1
            if c%2==1:
                if c!=1:
                    print(",",end=" ")
                print(i,end="")
    print(".")
    if c==0:
        print("No Palindrome Values.")