import sys
read=sys.stdin.readline

def is_prime(num):
    if num==1:
        return False
    rt=int(num**(0.5))
    for i in range(2,rt+1):
        if num%i==0:
            return False
    return True

ret=0
read()
arr=list(map(int,read().split()))
for num in arr:
    if is_prime(num):
        ret+=1
print(ret)