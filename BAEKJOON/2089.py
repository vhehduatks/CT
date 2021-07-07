import sys
read=sys.stdin.readline

N=int(read())

def recur(N):
    ret=''
    if N:
        if N%-2==-1:
            ret='1'
            N=N//-2+1
        else:
            ret='0'
            N=N//-2
    else:
        return ret
    return recur(N)+ret


if N==0:
    print('0')
else:
    print(recur(N))


