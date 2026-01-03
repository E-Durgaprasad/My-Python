"""Description:
Write a Program to Print the Following Pattern?
If Input is 5 then Print
2
2 3
2 3 5
2 3 5 7
2 3 5 7 11"""
def prime(i):
    if n<=1:
        return false
    for k in range(2,i):
        if i%k==0:
            return False
    return True
n=int(input("Enter number: "))
for i in range(1,n+1):
    c=2
    ok=True
    k=0
    while ok:
        if prime(c):
            print(c,end=" ")
            k+=1
        c+=1
        if k==i:
            ok=False
    print()