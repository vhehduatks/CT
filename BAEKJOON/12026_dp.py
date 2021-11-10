import sys
read=sys.stdin.readline

N=int(read())
block=list(read().strip())

dp=[sys.maxsize-1]*1001

def next_func(char):
    if char=='B':
        return 'O'
    elif char=='O':
        return 'J'
    else:
        return 'B'
dp[0]=0
for i in range(len(block)):
    next_char=next_func(block[i])
    for j in range(i,len(block)):
        if block[j]==next_char:
            dp[j]=min(dp[j],dp[i]+(j-i)**2)
ret=dp[len(block)-1]
print(ret if ret<sys.maxsize-1 else -1)