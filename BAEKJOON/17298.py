import sys


read=sys.stdin.readline
N=int(read())
arr=list(map(int,read().split()))
stack=[]
ret=[-1]*N
for i in range(N):
	while stack and stack[-1][0]<arr[i]:
		val,idx=stack.pop()
		ret[idx]=arr[i]
	stack.append((arr[i],i))

print(' '.join(list(map(str,ret))))