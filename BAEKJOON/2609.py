import sys
read=sys.stdin.readline

A,B=map(int,read().split())
C=max(A,B)
C=range(1,C+1)
temp=[]

for i in C:
    if A%i==0 and B%i==0:
        temp.append(i)

print(temp[-1])
print(int(A*B/temp[-1]))

