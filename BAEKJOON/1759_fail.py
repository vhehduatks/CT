import sys
from itertools import permutations
from string import ascii_lowercase
read=sys.stdin.readline

L,C=map(int,read().split())

arr=read().strip().split()
vowel=set(['a','e','i','o','u'])
consonant=set(ascii_lowercase)-vowel
ret=[]

def cnt_func(key):
	global vowel_cnt
	global consonant_cnt
	if key in vowel:
		vowel_cnt+=1
	if key in consonant:
		consonant_cnt+=1
	

for p in permutations(arr,L):
	vowel_cnt=0
	consonant_cnt=0
	fst=p[0]
	cnt_func(fst)
	is_order=True
	for s in range(1,L):
		cnt_func(p[s])
		if fst>p[s]:
			is_order=False
			break
		fst=p[s]
	if is_order:
		if vowel_cnt>0 and consonant_cnt>1:
			ret.append(''.join(p))

print('\n'.join(sorted(ret)))	
