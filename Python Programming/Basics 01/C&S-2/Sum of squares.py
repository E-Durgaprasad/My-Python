"""Description.:
Write a program to print sum of squares of the
numbers in given range .if starting range is Greater than
ending range print "INVALID RANGE"
Constraints:
Input : First line of input contains a integer that denotes strating range

Second line. of input contains a integer that denotes ending range

Output :Integer that denotes sum
Example:
Input : 5
        23
Output :4294
Explanation :
52 + 62 + 72 + 82 + 92 + 102 + 112 + 122 + 132 + 142 + 152 + 162 + 172 + 182 + 192 + 202 + 212 + 222 + 232
=25 + 36 + 49 + 64 + 81 + 100 + 121 + 144 + 169 + 196 + 225 + 256 + 289 + 324 + 361 + 400 + 441 + 484 + 529
=4294
"""
n=int(input("Enter a number:"))
m=int(input("Enter a number:5"))
sum=0
if n>m:
    print("INVALID RANGE")
else:
    for i in range(n,m+1):
        sum=sum+i**2
    print(sum,end=" ")