# Write a program to find sum of Factorials upto N Numbers like 0! + 1! + 2! + 3! + 4! + 5! +....upto n!?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Sum of Factorials upto N Numbers.
# Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "INvalid INput".
# Example:
# Input 1  :    6
# Output 1:    1+1+2+6+24+120+720=874
n=int(input("Enter Number:"))
count=0
sum=0
if n<0:
    print("INvalid INput")
else:
    for i in range(0,n+1):
            fact=1
            for j in range(1,i+1):
                fact=fact*j
            count+=1
            sum=sum+fact
            if count!=1:
                print("+",end="")
            print(fact,end="")
    print(f"={sum}")