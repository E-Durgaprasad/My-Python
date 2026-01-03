"""Write a Program to Print the Following Pattern?
If Input is 4 then Print
1
2 4
3 6 9
4 8 12 16
5 10 15
6 12
7   """
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    c=1
    for j in range(1,i+1):
        print(c*i,end=" ")
        c+=1
    print()
k=n+1
for i in range(1,n):
    for j in range(1,n-i+1):
        print(k*j,end=" ")
    k+=1
    print()