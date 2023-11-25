# Write a program to print maximum of each column from the matrix

n=int(input())
A=[]
for i in range(0,n):
    l=list(map(int,input().split()))
    A.append(l)
for i in range(0,n):
    max=0
    for j in range(0,n):
        if A[j][i]>max:
            max=A[j][i]
    print(max,end=' ')
