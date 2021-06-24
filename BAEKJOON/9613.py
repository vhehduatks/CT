import sys
read=sys.stdin.readline

c=int(read())

def gcd(a,b):
    while(b>0):
        r=a%b
        a=b
        b=r
    return a

for _ in range(c):
    ret=0
    temp=list(map(int,read().split()))
    temp.pop(0)
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            ret+=gcd(temp[i],temp[j])
    print(ret)

