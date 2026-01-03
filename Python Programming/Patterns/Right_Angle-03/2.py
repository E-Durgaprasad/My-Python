"""Write a Program to Print the Following Pattern
If Input is 5 and 3 then Print
3
44
555
6666
77777"""
n,m=map(int,input("Enter a number: ").split())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(m,end="")
    m+=1
    print()
