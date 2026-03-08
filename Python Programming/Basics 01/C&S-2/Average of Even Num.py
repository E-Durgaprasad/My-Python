"""Description:
Write a program to find the average of all even numbers in the given range
.if the strating range is Greater than ending range then print
"INVALID RANGE"
Constraints:
Input :First line of input contains Integer which denotes starting range
Second line of input contains Integer which denotes ending range

Example:.
Input :10
    30
Output : 20.0

Explanation:
in the above example even numbers in range are 10,12,14,16,18,20,22,24,26,28,30
avarage of those numbers is 20.0"""

n=int(input("Enter number:"))
m=int(input("Enter number:"))
sum=0
avg=0
for i in range(n,m+1):
    if i%2==0:
        sum=sum+i
        avg=avg+1
print(sum/avg)