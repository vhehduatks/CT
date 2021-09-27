import sys
read=sys.stdin.readline

V,E=map(int,read().split())
tree_tuple=[]
p=[i for i in range(10001)]
for i in range(E):
    A,B,weight=map(int,read().split())
    tree_tuple.append((A,B,weight))


tree_tuple.sort(key=lambda x:x[2])
MinTree=[]
MTW=0
MTWE=0

def find(i):
    if i!=p[i]:
        p[i]=find(p[i])
    return p[i]

def union(i,j):
    root1=find(i)
    root2=find(j)
    p[root1]=root2

while(MTWE<V-1):
    
    A,B,weight=tree_tuple.pop(0)
    if find(A)!=find(B):
        union(A,B)
        MTW+=weight
        MTWE+=1


print(MTW)