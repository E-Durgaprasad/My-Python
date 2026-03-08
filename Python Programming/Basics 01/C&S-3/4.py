# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Following Series.
# Constraints  :- No
# Input 1  :    10
# Output 1:    1, 2, factor of three, 4, 5, factor of three, 7, 8, factor of three, 10
n=int(input("Enter Numbers:"))
c=0
for i in range(1,n+1):
    c=c+1
    if c!=1:
            print(", ",end="")
    if i%3==0:
        print("factor of three",end="")
    else:
        print(i,end="")