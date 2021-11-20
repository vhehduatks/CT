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

for i in arr:
    if lis[-1]<i:
        lis.append(i)
    else:
        lis[bin_search(0,len(lis),i)]=i

print(len(lis))