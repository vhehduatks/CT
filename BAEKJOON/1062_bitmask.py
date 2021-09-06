import sys
import string
read=sys.stdin.readline


N,K=map(int,read().split())
convert_word=[]
base=set(['a','n','t','i','c'])
Ascii_lc=list(string.ascii_lowercase)
new_Ascii=list(set(string.ascii_lowercase).difference(base))

for _ in range(N):
    word=set(read().strip()[4:-4]).difference(base)
    bin=0
    for w in word:
        bin=bin|(1<<Ascii_lc.index(w))
    convert_word.append(bin)

def comb(a,n=K-5):
    result=[]
    ret=[]
    def recur(nextarr):
        if len(result)==n:
            ret.append(result[:])
            return
        if not nextarr:
            return
        
        temp=nextarr[:]
        for i in nextarr:
            result.append(i)
            temp.remove(i)
            recur(temp)
            result.pop()

    recur(a)
    return ret

if K>=5:
    Combs=comb(new_Ascii)

    max_count=0
    for Comb in Combs:
        count=0
        comb_bin=0
        for c in Comb:
            comb_bin=comb_bin|(1<<Ascii_lc.index(c))
        for cw in convert_word:
            if cw & comb_bin ==cw:
                count+=1
        max_count=max(max_count,count)

    print(max_count)
else:
    print(0)