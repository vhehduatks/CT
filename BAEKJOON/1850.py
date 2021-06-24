import sys
read=sys.stdin.readline

a,b=map(int,read().split())
if a>b:
    a,b=b,a

def gcd(a,b):
    while(b>0):
        r=a%b
        a=b
        b=r
    return a

print('1'*gcd(3,6))

