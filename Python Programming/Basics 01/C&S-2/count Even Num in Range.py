"""Description:
Write a program to find the count of even numbers in given range.if no even numbers print NO NUMBERS
if Strating range is greater than ending range print INVALID RANGE
Constraints:
Input :  First line of input contains Integer n represent staring range
         Second line of input contains Integer n1 represent ending range
Output :  Print Count of the All even Numbers in a Given Range
Example:.
Input :10
        20
Output :   6
"""
n=int(input("Enter Number:"))
m=int(input("Enter Number:"))
if n>m:
    print("INVALID RANGE")
else:
    c=0
    for i in range(n,m+1):
        if i%2==0:
            c=c+1
    if c==0:
        print("NO EVEN NUMBERS")
    else:
        print(c)



