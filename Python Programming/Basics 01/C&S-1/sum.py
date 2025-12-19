"""Write a program to find sum of all the numbers
in given range if starting index
is greater than ending index print INVALID RANGE"""

x=int(input("Enter range: "))
y=int(input("Ending range: "))
sum=0
for i in range(x,y+1):
    sum=sum+i
s=0
if x>y:
    print("INVALID RANGE")
else:
    for i in range(x,y+1):
        s+=i
    print(s)