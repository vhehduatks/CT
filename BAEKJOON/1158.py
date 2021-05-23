import sys
read=sys.stdin.readline

N,K=map(int,read().split())

temp=list(range(1,N+1))
num=N
ptr=K-1

print('<',end='')
print(temp.pop(ptr),end='')
while temp:
    num-=1
    ptr=(ptr+(K-1))%num
    print(', {}'.format(temp.pop(ptr)),end='')
print('>')