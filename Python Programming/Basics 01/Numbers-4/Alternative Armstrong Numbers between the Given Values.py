# Description:
# Write a program to print the Alternative Armstrong Numbers between the Given Values?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#           Second Line of Input Consists of One Integer Value.
# Output        :- Print the All Alternative Armstrong Numbers.
# Constraints  :- Either of the Given Inputs is Equal to Zero then Print "Invalid Inputs".
#                       If there is No Armstrong Numbers Between the Given Values then print "No Armstrong Numbers Between Given Values.".
#                       If Either of the Given Inputs is Negative then Convert into Positive and then Print the Alternative Armstrong Numbers.
# Input 1  :    1
#                   200
# Output 1:    Alternative Armstrong Numbers between the Given Values is 2, 4, 6, 8, 153.
def arm(i):
    c,t=0,i
    while t>0:
        r=t%10
        c+=1
        t=t//10
    t,sum=i,0
    while t>0:
        r=t%10
        sum=sum+r**c
        t=t//10
    return sum==i
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
    count=0
    for i in range(n+1,m):
        if arm(i):
            count+=1
            if count%2==1:
                if count==1:
                    print("Alternative Armstrong Numbers between the Given Values is ",end="")
                if count!=1:
                    print(",",end=" ")
                print(i,end="")
    if count==0:
        print("No Armstrong Numbers Between Given Values.",end="")
    else:
        print(".")