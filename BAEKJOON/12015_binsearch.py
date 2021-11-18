import sys
read=sys.stdin.readline

N=int(read())
arr=list(map(int,read().split()))

lis=[]
lis.append(arr[0])
def bin_search(start,end,target):

    while start<end:
        mid=(end+start)//2
        if lis[mid]<target:
            start=mid+1
        else:
            end=mid
    return end


end=len(lis)

for i in range(len(arr)):
    if lis[-1]<arr[i]:
        lis.append(arr[i])
        end=len(lis)
    else:
        idx=bin_search(0,end,arr[i])
        lis[idx]=arr[i]
        
print(len(lis))
