import sys
import string
read=sys.stdin.readline
ascii=string.ascii_lowercase

ret=[-1]*26
word=read().strip()

for i,a in enumerate(word):
    ret[ascii.index(a)]=i if ret[ascii.index(a)]==-1 else ret[ascii.index(a)]

for i in ret:
    print(i,end=' ')