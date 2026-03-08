"""Write a program to print all Odd Numbers in Given Range.
if starting range is greater than ending range print
"INVALID RANGE"
Constraints:
Input :First line of input contains Integer n represent starting index
    Second line of input contains Integer n1 represents ending index
Output :Print All the Odd Numbers in a Given Range
Example:.
Input :1
        10
Output :1 3 5 7 9
"""
n=int(input("Enter Number:"))
m=int(input("Enter Number:"))
for i in range(n,m+1):
    if i%2==1:
        print(i,end=" ")

