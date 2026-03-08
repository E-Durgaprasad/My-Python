# Write a program to print First N terms of Alternative Fibonacci Series?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the First N terms of Alternative Fibonacci Series.
# Constraints  :- Given Input is Equals to Zero then Print "Invalid Input".
#         If the input number is negative, convert it to positive first, then generate and print the Fibonacci series
# Input 1  :    10
#
# Output 1:    0, 1, 3, 8, 21, 55, 144, 377, 987, 2584
n=int(input("Enter Number:"))
if n==0:
    print("Invalid Input")
else:
    if n<0:
        n=abs(n)
    a,b=0,1
    count=0
    sum=0
    ac=0
    for i in range(2*n):
            count+=1
            if count%2==1:
                ac+=1
                if count!=1:
                    print(",",end=" ")
                print(a,end="")
            c=a+b
            a=b
            b=c