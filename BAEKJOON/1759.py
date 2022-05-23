import sys
from itertools import combinations
read=sys.stdin.readline

L,C=map(int,read().split())

arr=read().strip().split()
arr.sort()

for c in combinations(arr,L):
	if 0<c.count('a')+c.count('e')+c.count('i')+c.count('o')+c.count('u')<L-1:
		print(''.join(c))