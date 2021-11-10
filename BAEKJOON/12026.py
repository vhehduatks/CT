import sys
read=sys.stdin.readline

N=int(read())
block=list(read().strip())

ret=0
i=0
while(True):
    try:
        if i==len(block)-1:
            break
        if block[i]=='B':
            k=block[i:].index('O')
            ret+=k**2
            i+=k
        elif block[i]=='O':
            k=block[i:].index('J')
            ret+=k**2
            i+=k
        elif block[i]=='J':
            k=block[i:].index('B')
            ret+=k**2
            i+=k
    except:
        ret=-1
        break

print(ret)