"""Write a Program to Print the Following Pattern?
If Input is 5 then Print

1
3*2
4*5*6
10*9*8*7
11*12*13*14*15"""

# n=int(input("Enter a number: "))
# c=1
# for i in range(1,n+1):
#     k=0
#     for j in range(1,i+1):
#         if i%2==1:
#             k+=1
#             if k!=1:
#                 print("*",end="")
#             print(c,end="")
#             c+=1
#         else:
#             if j==1:
#                 v=c+i-1
#             k=k+1
#             if k!=1:
#                 print("*",end="")
#             print(v,end="")
#             v=v-1
#             c=c+1
#     print()

"""---another method---"""


n = int(input("Enter a number: "))
c= 1
for i in range(1, n + 1):
    row = []
    for j in range(i):
        row.append(str(c))
        c += 1
    if i % 2 == 0:
        row.reverse()
    print("*".join(row))
