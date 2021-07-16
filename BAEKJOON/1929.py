import sys
read=sys.stdin.readline

M,N=map(int,read().split())

def is_prime(num):
    if num==1:
        return False
    rt=int(num**(0.5))
    for i in range(2,rt+1):
        if num%i==0:
            return False
    return True

for i in range(M,N+1):
    if is_prime(i):
        print(i)

        
