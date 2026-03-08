# Write a program to check Whether the Given Number(any number of digits) is Armstrong or Not.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print if the number is an Armstrong Number or Not a Armstrong Number.
# Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input".
# Input 1  :    253
# Output 1:    253 is Not a Armstrong Number.
a=int(input("Enter Number:"))
if a<=0:
    print("Invalid Input")
else:
    c,t=0,a
    while t>0:
        r=t%10
        c+=1
        t=t//10
    sum,t=0,a
    while t>0:
        r=t%10
        sum=sum+r**c
        t=t//10
    if  sum==a:
        print(f"{a} is a Armstrong Number.")
    else:
        print(f"{a} is Not a Armstrong Number.")