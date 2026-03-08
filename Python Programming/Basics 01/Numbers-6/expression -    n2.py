# Write a Program to Find the result of the following expression -
#  + ........... 16 + 9 + 4 + 1=?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Following Format.
# Constraints  :- Given Input is equal to Zero then Print "Invalid Input".
# Input 1  :    9
# Output 1:    81 + 64 + 49 + 36 + 25 + 16 + 9 + 4 + 1 = 285
n=int(input("Enter Number:"))
sum=0
count=0
if n==0:
    print("Invalid Input")
else:
    if n<0:
        n=abs(n)
    while n>0:
        sum=sum+n**2
        count+=1
        if count!=1:
            print(" + ",end="")
        print(n**2,end="")
        n=n-1
    print(f" = {sum}",end="")