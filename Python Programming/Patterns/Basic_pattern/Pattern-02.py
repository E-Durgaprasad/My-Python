"""Write a Program to Print the following Basic Pattern?

If Input is 5 then Print

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5"""
n=int(input("Enter value: "))
if n<=0:
    print("InValid InPut")
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,end=" ")
        print()