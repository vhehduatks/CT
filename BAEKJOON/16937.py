import sys
read=sys.stdin.readline

H,W=map(int,read().split())
N=int(read())
stiker=[]
for _ in range(N):
	R,C=map(int,read().split())
	stiker.append([R,C])

from itertools import combinations

ret=0
def is_in(s1,s2,b):
	if s1+s2<=b:
		return True
	return False

def calc(box1,box2):
	ret=0
	if is_in(box1[0],box2[0],H):
		if box1[1]<=W and box2[1]<=W:
			ret=max(ret,box1[0]*box1[1]+box2[0]*box2[1])
	if is_in(box1[1],box2[1],W):
		if box1[0]<=H and box2[0]<=H:
			ret=max(ret,box1[0]*box1[1]+box2[0]*box2[1])
	return ret

ret=0
for c in combinations(range(N),2):
	box1,box2=c
	box1,box2=stiker[box1],stiker[box2]
	# 0,0 (회전여부) 
	ret=max(ret,calc(box1,box2))
	
	# 1,0
	box1_=[box1[1],box1[0]]
	ret=max(ret,calc(box1_,box2))
	
	# 0,1
	box2_=[box2[1],box2[0]]
	ret=max(ret,calc(box1,box2_))

	# 1,1
	ret=max(ret,calc(box1_,box2_))

print(ret)