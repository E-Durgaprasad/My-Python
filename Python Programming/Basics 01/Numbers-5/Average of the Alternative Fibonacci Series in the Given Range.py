# Write a program to print the Average of the Alternative Fibonacci Series in the Given Range?
#
#
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#
#                      Second Line of Input Consists of One Integer Value.
#
# Output        :- Print the Average of Fibonacci Series in the Given Range.
#
# Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "Invalid Inputs".
#
#                      If there are no Fibonacci Series values in the Given Range then Print, "No Fibonacci Series Values".
# Input 1  :    13
#
#                   91
#
# Output 1:    45.33
n=int(input("EnterNumber:"))
m=int(input("Enter Number:"))
sum=0
count=0
acount=0
if n<0 or m<0:
    print("Invalid Inputs")
else:
    if n>m:
        n,m=m,n
    a,b=0,1
    while a<=m:
        if a>=n:
            count+=1
            if count%2==1:
                acount+=1
                sum=sum+a
        c=a+b
        a=b
        b=c
    if count==0:
        print("No Fibonacci Series Values")
    else:
        avg=sum/acount
        print(f"{avg:.2f}")