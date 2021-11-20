import sys
read=sys.stdin.readline

N=int(read())
arr=list(map(int,read().split()))
lis=[arr[0],]

def bin_search(s,e,t):
    while s<e:
        m=(s+e)//2
        if lis[m]<t:
            s=m+1
        else:
            e=m
    return e
lis_idx=[]
for i in arr:
    if lis[-1]<i:
        lis.append(i)
        lis_idx.append(len(lis)-1)
    else:
        idx=bin_search(0,len(lis),i)
        lis[idx]=i
        lis_idx.append(idx)


print(len(lis))
idx=len(lis)-1
temp=[]
for i in reversed(range(N)):
    if lis_idx[i]==idx:
        temp.insert(0,arr[i])
        idx-=1
print(" ".join(map(str,temp)))
