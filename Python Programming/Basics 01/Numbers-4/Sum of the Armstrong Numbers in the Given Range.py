# Write a program to print the Sum of the Armstrong Numbers in the Given Range?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the Sum of All Armstrong Numbers.
# Constraints  :- Either of the Given Input is Equal to Zero then Print "Invalid Inputs".
#            If there are No Armstrong Numbers Between the Given Range then, print "No Armstrong Numbers in a Given Range.".
#                       If Either of the Given Inputs is Negative then Convert into Positive and then Print the Sum of all Armstrong Numbers.
# Input 1  :    1
#           200
# Output 1:    Armstrong Numbers in the Given Range is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 153 = 198.
def is_arm(i):
    t,c=i,0
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
a=int(input("Enter number:"))
b=int(input("Enter Number:"))
if a==0 or b==0:
    print("Invalid Inputs")
else:
    if a<0:
        a=abs(a)
    if b<0:
        b=abs(b)
    if a>=b:
        a,b=b,a
    count=0
    sum=0
    for i in range(a,b+1):
        if is_arm(i):
            sum=sum+i
            count+=1
            if count==1:
                print("Armstrong Numbers in the Given Range is ",end="")
            if count!=1:
                print(" +",end=" ")
            print( i ,end="")
    print(f" = {sum}",end="")
    if count==0:
        print("No Armstrong Numbers in a Given Range.")
    else:
        print(".")