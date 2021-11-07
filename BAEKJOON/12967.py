import sys
read=sys.stdin.readline

N,K=map(int,read().split())
templist=list(map(int,read().split()))

def gcd(a,b):
    if a<b:
        a,b=b,a
    while(b>0):
        r=a%b
        a,b=b,r

    return a

gcd_list=[]
for i in templist:
    gcdnum=gcd(K,i)
    if gcdnum!=1:
        gcd_list.append(gcdnum)

def comb(arr,num):
    res=[]
    ret=[]
    
    def recur(next):
        if len(res)==num:
            ret.append(res[:])
            return
        if not next:
            return
        
        temp=next[:]
        for i in next:
            res.append(i)
            temp.remove(i)
            recur(temp)
            res.pop()
    recur(arr)
    return ret

cnt=0
for p,q,r in comb(gcd_list,3):
    if p*q*r%K==0:
        cnt+=1

print(cnt)
