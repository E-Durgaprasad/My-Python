# Write a program to find Sum of first 'n' Natural Numbers Without Using formula?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print Sum of first 'N' Natural Numbers.
# Constraints  :- Given Input is Zero then Print "InvaLid Input.".
#                       If Given Input is Negative then Print "Sorry! you have Entered Negative Values.".
# Input 1  :    10
# Output 1:    Sum of 'N' Natural Numbers is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.
n=int(input("Enter Number:"))
if n==0:
    print("Invalid Input.")
elif n<=0:
    print ("Sorry! you have Entered Negative Values.")
else:
    c=0
    sum=0
    for i in range(1,n+1):
        c+=1
        if c==1:
            print("Sum of 'N' Natural Numbers is ",end="")
        if c!=1:
            print(" + ",end="")
        print(i,end="")
        sum=sum+i
    print(f" = {sum}.")