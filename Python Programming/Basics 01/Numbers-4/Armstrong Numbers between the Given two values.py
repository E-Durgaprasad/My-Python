# Write a program to print the Armstrong Numbers between the Given two values.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the All Armstrong Numbers.
# Constraints  :- Either of the Given Inputs is Equal to Zero then Print "Invalid Inputs".
#              If there are No Armstrong Numbers Between the Given Values then print "No Armstrong Numbers Between Given Values".
#       If Either of the Given Inputs is Negative then Convert into Positive and then Print the Armstrong Numbers.
# Input 1  :    1
#              200
# Output 1:    Armstrong Numbers between the Given Values is 2, 3, 4, 5, 6, 7, 8, 9, 153.

def arm(i):
    t,dc=i,0
    while t>0:
        r=t%10
        dc+=1
        t=t//10
    sum,t=0,i
    while t>0:
        r=t%10
        sum=sum+r**dc
        t=t//10
    return sum==i
a=int(input("Enter Number:"))
b=int(input("Enter number:"))
if a==0 or b==0:
    print("Invalid Inputs")
else:
    if a<0:
        a=abs(a)
    if b<0:
        b=abs(b)
    if a>b:
        a,b=b,a
    count=0
    for i in range(a+1,b):
        if arm(i):
            count+=1
            if count==1:
                print("Armstrong Numbers between the Given Values is ",end="")
            if count!=1:
                print(", ",end="")
            print(i,end="")
    else:
        if count==0:
            print("No Armstrong Numbers Between Given Values",end="")
        else:
            print(".")