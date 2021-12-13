import sys
read=sys.stdin.readline

N,S=map(int,read().split())

def gcd(a,b):
	if a>b:
		a,b=b,a
	while(a>0):
		r=b%a
		b,a=a,r
	return b

A=list(map(int,read().split()))
temp=[]
for i in A:
	if abs(S-i):
		temp.append(abs(S-i))
if len(temp)>1:
	GCD=gcd(temp.pop(),temp.pop())

	while temp:
		GCD=gcd(temp.pop(),GCD)

	print(GCD)
else:
	print(temp[0])