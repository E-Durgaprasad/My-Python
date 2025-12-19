"""Write a program to print all even numbers in range.
if starting range is greater than ending range print "INVALID RANGE"""""

n=int(input("Enter starting number: "))
m=int(input("Enter ending number: "))
if n>m:
    print("INVALID RANGE")
for i in range(n,m+1):
        if i%2==0:
            print(i,end=" ")