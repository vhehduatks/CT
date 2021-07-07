import sys
read=sys.stdin.readline

binary=['0','1','2','3','4','5','6','7','8','9',
        'A','B','C','D','E','F','G','H','I','J',
        'K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z']

N,B=read().strip().split()
N=list(N)
ret=0
while(N):
    N_len=len(N)-1
    temp=N.pop(0)
    ret+=(int(B)**N_len)*binary.index(temp)
print(ret)
    
