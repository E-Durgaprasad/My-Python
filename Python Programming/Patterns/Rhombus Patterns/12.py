"""Write a Program to Print the Following Pattern?
If Input is 4 and 2 then Print
2
3 3
4 4 4
5 5 5 5
5 5 5 5
4 4 4
3 3
2

"""
n=int(input("Enter the number: "))
s=int(input("Enter the starting number: "))
for i in range(1,n+1):
        for j in range(1,i+1):
            print(s,end=" ")
        s+=1
        print()
for i in range(1,n+1):
    s-=1
    for j in range(1,n-i+2):
        print(s,end=" ")
    print()
