import sys
sys.setrecursionlimit(10**6)
read=sys.stdin.readline



def bins(s,e,n):
	while s<e:
		mid=(s+e)//2
		if pnl[mid]<n:
			s=mid+1
		else:
			e=mid
	return e
		

def gold(idx):
	global res
	if res:
		return 1
	elif idx<0:
		return 0
	i=0
	while n>=(pnl[idx]+pnl[i]):
		if pnl[idx]+pnl[i]==n:
			res.append((pnl[idx],pnl[i]))
			return
		i+=1
	gold(idx-1)

maxn=1100000
boollist=[False,False]+[True]*(maxn+1)
pnl=[]
for i in range(2,maxn+1):
	if boollist[i]:
		pnl.append(i)
		for j in range(2*i,maxn+1,i):
			boollist[j]=False

n=int(read())
while n!=0:
	idx=bins(0,len(pnl),n)
	res=[]
	gold(idx)
	if res:
		i1,i2=res[0]
		print('{} = {} + {}'.format(n,i2,i1))
	else:
		print("Goldbach's conjecture is wrong.")
	n=int(read())