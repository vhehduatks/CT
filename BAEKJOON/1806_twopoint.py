import sys
read=sys.stdin.readline

N,S=map(int,read().split())
Arr=list(map(int,read().split()))

Sum=0
Count=sys.maxsize-1
end=0
for start in range(len(Arr)):
    while Sum<S and end<len(Arr):
        Sum+=Arr[end]
        end+=1
    if Sum>=S:
        Count=min(Count,end-start)
    Sum-=Arr[start]

print(0 if Count==sys.maxsize-1 else Count)
    