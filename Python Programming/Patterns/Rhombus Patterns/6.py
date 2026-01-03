"""Write a Program to Print the Following Pattern?
If Input is 5 and 3 then Print
3
44
555
6666
77777
6666
555
44
3 """
n=int(input("Enter the input: "))
s=int(input("Enter the starting value: "))
c=s
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end="")
    c+=1
    print()
    k=c-2
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(k,end="")
    k-=1
    print()