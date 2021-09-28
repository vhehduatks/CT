import sys
import string
read=sys.stdin.readline
ascii=string.ascii_lowercase
full_str=read()
find_str=read()

def rabinkarp(P,S):
    P_len=len(P)-1
    S_len=len(S)-1
    P_hash=0
    S_hash=0
    power=1

    i=0
    while S[i]!='\n':
        P_hash+=ascii.index(P[i])*power
        S_hash+=ascii.index(S[i])*power
        power*=2
        i+=1
    power//=2

    i=0
    while P[S_len]!='\n':
        if i==0:
            if P_hash==S_hash:
                return 1
        else:
            P_hash=(P_hash-ascii.index(P[i-1]))//2+ascii.index(P[S_len])*power
            S_len+=1
            if P_hash==S_hash:
                return 1
        i+=1

    return 0

print(rabinkarp(full_str,find_str))    