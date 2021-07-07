import sys
read=sys.stdin.readline

N=list(read().strip())

str_ret=''
while(N):
    count=0
    ret=0
    while(count<3):
        try:
            ret+=(2**count)*int(N.pop())
        except:
            break
        count+=1
    str_ret+=str(ret)

print(str_ret[::-1])

