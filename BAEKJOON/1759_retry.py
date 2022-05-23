import sys

read=sys.stdin.readline

l,c=map(int,read().split())
arr=read().strip().split()
arr.sort()

ret=[]
def recur(depth):
	if len(ret)==l:
		if 0<ret.count('a')+ret.count('e')+ret.count('i')+ret.count('o')+ret.count('u')<l-1:
			print(''.join(ret))
		return	
	for i in range(depth,c):
		ret.append(arr[i])
		recur(i+1) # 처음에 for문은 0부터 c까지 가는데 그럼 for문이 1 일때 depth가 0 이면 arr[1]이 두번 들어갈 수 있음 
		ret.pop()

recur(0)





